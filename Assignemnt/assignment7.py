
"""
Console Output

Please enter a filename (e.g.: /path/to/filename) : dat.txt

File report :

Number of lines:  3
Number of words:  13
Number of characters:  54

------------------------------
FILE OBJECT
------------------------------
Please enter a filename (e.g.: /path/to/filename) : ./samples/dat.txt
File ./samples/dat.txt is not found.
Please enter a filename (e.g.: /path/to/filename) : ./dat.txt

File report :./dat.txt
Number of lines: 3
Number of words: 13
Number of characters: 54
Number of spaces: 12

------------------------------
DICTIONARY OBJECT
------------------------------
Please enter a file path (e.g.: /path/to/directory) : ./samples/
Total files in ./samples/: 3
File report :./samples/test3.txt
Number of lines: 2
Number of words: 19
Number of characters: 92
Number of spaces: 19
File report :./samples/test1.txt
Number of lines: 3
Number of words: 13
Number of characters: 55
Number of spaces: 12
File report :./samples/test2.txt
Number of lines: 5
Number of words: 42
Number of characters: 214
Number of spaces: 53

Process finished with exit code 0

"""
import re as regex
from os import listdir
from os.path import isfile, join


def read_file_from_user():
    """
    Ask user to enter a file and process the file:
    :return: a list contain 3 integers :
            1st int: number of lines
            2nd int: number of words
            3rd int: number of characters in the file
    """
    user_input = get_file_name()
    f = open_file(user_input)
    num_lines = 0
    num_words = 0
    num_chars = 0

    with f as input_file:
        for line in input_file:
            num_lines += 1
            inline_words = line.split()
            num_words += len(inline_words)
            for word in inline_words:
                num_chars += len(word)
    f.close()
    return [num_lines, num_words, num_chars]


def get_file_name():
    """
    Read filename from user
    :return: a string : filename
    """

    # Practice regular expression and try/catch in Python
    correct_file_pattern = regex.compile(".+\..+")
    while True:
        try:
            filename = input("Please enter a filename (e.g.: /path/to/filename) : ")

            if not correct_file_pattern.match(filename):
                raise CustomException("Invalid file name")
        except CustomException as e:
            print(e, "Please try again")
        except Exception as e:
            print(e, "Please try again")
        else:
            return filename


def open_file(file_name):
    """
    Open file using provided filename
    :param file_name: a string contains path to file
    :return: file object
    """
    while True:
        try:
            file = open(file_name)
        except FileNotFoundError:
            print("File", file_name, "is not found.")
            file_name = get_file_name()
        except Exception as e:
            print(e)
            file_name = get_file_name()
        else:
            return file


def get_path_name():
    """
    Read file path from user
    :return: a string : filename
    """

    # Practice regular expression and try/catch in Python
    correct_path_pattern = regex.compile("^(/)?([^/\0]+(/)?)+$")
    while True:
        try:
            file_path = input("Please enter a file path (e.g.: /path/to/directory) : ")
            if not correct_path_pattern.match(file_path):
                raise CustomException("Invalid file path")

        except CustomException as e:
            print(e, "Please try again")
        else:
            return file_path


class CustomException(Exception):
    pass


class File:
    """
    File object. Analyze stat for each file object such as lines, spaces
    """
    def __init__(self, filename):
        self.file_name = filename
        self.num_lines = 0
        self.num_words = 0
        self.num_spaces = 0
        self.num_chars = 0

    def count(self):
        """
        Ask user to enter a file and process the file:
        :return: a list contain 3 integers :
                1st int: number of lines
                2nd int: number of words
                3rd int: number of characters in the file
        """
        f = open_file(self.file_name)
        space_regex = regex.compile('\s')
        with f as input_file:
            for line in input_file:
                self.num_lines += 1
                inline_words = line.split()
                inline_spaces = space_regex.findall(line)
                self.num_words += len(inline_words)
                self.num_spaces += len(inline_spaces)
                for word in inline_words:
                    self.num_chars += len(word)
        f.close()

    def open_file(self):
        """
        Open file using provided filename
        :param
        :return: file object
        """
        while True:
            try:
                file = open(self.file_name)
            except FileNotFoundError:
                print("File", self.file_name, "is not found.")
                self.file_name = get_file_name()
            except Exception as e:
                print(e)
                self.file_name = get_file_name()
            else:
                return file

    def __get_file_name(self):
        """
        Read filename from user - Private method
        :return: a string : filename
        """

        # Practice regular expression and try/catch in Python
        correct_path_pattern = regex.compile("^(/)?([^/\0]+(/)?)+$")
        correct_file_pattern = regex.compile(".+\..+")
        while True:
            try:
                filename = input("Please enter a filename (e.g.: /path/to/filename) : ")

                if not correct_file_pattern.match(filename):
                    raise CustomException("Invalid file name")

                elif not correct_path_pattern.match(filename):
                    raise CustomException("Invalid file path")

            except CustomException as e:
                print(e, "Please try again")
            except Exception as e:
                print(e, "Please try again")
            else:
                self.file_name = filename

    def __str__(self):
        """
        Return stats for current file
        :return: a string
        """
        toString = "\nFile report :" + self.file_name
        toString +='\nNumber of lines: '+ str(self.num_lines)
        toString +="\nNumber of words: "   + str(self.num_words)
        toString +="\nNumber of characters: "+ str(self.num_chars)
        toString +="\nNumber of spaces: "  + str(self.num_spaces)

        return toString


class Directory:
    """

    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.num_files = 0
        self.file_str_list = []
        self.files = []

    def count(self):
        """
        Analyze stat on each file in the current directory
        :return: nothing
        """
        self.__get_file_list()

        for fl in self.file_str_list:
            a_file = File(fl)
            a_file.count()
            self.files.append(a_file)

    def __get_file_list(self):
        """
        Parse all the files in directory into a list
        :return: self.files will contain list of files in current dir
        """
        correct_path_pattern = regex.compile("^(/)?([^/\0]+(/)?)+$")

        while True:
            try:
                if not correct_path_pattern.match(self.file_path):
                    raise CustomException("Invalid file path")
            except CustomException as e:
                print(e, "Please try again")
                self.get_path_name()

            else:
                try:
                    self.file_str_list = [join(self.file_path, f) for f in listdir(self.file_path) if isfile(join(self.file_path, f))]
                    self.num_files = len(self.file_str_list)
                except FileNotFoundError:
                    print("Directory is empty")
                break

    def __get_path_name(self):
        """
        Read file path from user
        :return: a string : filename
        """

        # Practice regular expression and try/catch in Python
        correct_path_pattern = regex.compile("^(/)?([^/\0]+(/)?)+$")
        while True:
            try:
                self.file_path = input("Please enter a file path (e.g.: /path/to/directory) : ")
                if not correct_path_pattern.match(self.file_path):
                    raise CustomException("Invalid file path")

            except CustomException as e:
                print(e, "Please try again")
            except Exception as e:
                print(e, "Please try again")
            else:
                break

    def __str__(self):
        """

        :return: a string
        """
        to_str = "Total files in " + self.file_path + ": " + str(self.num_files)
        for fl in self.files:
            to_str += str(fl)
        return to_str
if __name__ == "__main__":

    stats = read_file_from_user()
    if stats:
        print("\nFile report :")
        print("\nNumber of lines: ", str(stats[0]))
        print("Number of words: ", str(stats[1]))
        print("Number of characters: ", str(stats[2]))

    print("\n------------------------------")
    print("FILE OBJECT")
    print("------------------------------")
    test_file_name = get_file_name()
    file_object = File(test_file_name)
    file_object.count()
    print(str(file_object))

    print("\n------------------------------")
    print("DICTIONARY OBJECT")
    print("------------------------------")
    test_path = get_path_name()
    directory_object = Directory(test_path)
    directory_object.count()
    print(str(directory_object))


"""
Write a program that asks the user for a filename, opens the file and reads through the file just once
before reporting back to the user:
- the number of characters (including spaces and end of line characters),
- the number of words,
- the number of lines in the file.

If the user enters the name of a file that doesn't exist, your program should give her as many tries as she needs in
order to type a valid filename.

Obtaining a valid filename from the user is a common operation, so start by writing a separate, reusable function that
repeatedly asks the user for a filename until she types in a file that your program is able to open.

This separate, reusable function will then return the opened file as its returned value.
You will be able to reuse this function later in the quarter.

Please submit to me THREE things:

1. Your source code file
2. A recording of the run (which may be at the bottom of your source code file)
3. The external data file that you used to test your program with.

Hints:
• You only need to read through the file one time in order to compile the three statistics required.
• In order to count the number of words you might find the following string methods helpful:
https://docs.python.org/3.1/library/stdtypes.html#string-methods (Links to an external site.)
Note that because the methods listed at the above URL are METHODS, you call them with the object at the left side of
the "." instead of sending the object in as parameter.
For example:
myString.lower()
returns the lower case version of myString.

In order to receive full credit:
1. Define a separate function that reads the filename from the user and opens the file.
2. Make sure your program doesn't crash if the filename the user enters doesn't exist.
3. Your program must read through the file just once in order to compile all three statistics


2.  Now expand the program to be object Oriented, create a file class that contains variables/properties for number of
characters, number of spaces, lines, words etc.

The file class should implement all these properties/variables
The file should also implement the necessary methods to read the number of characters, number of words, spaces, lines etc.
Create a directory class that will contain a list of file objects, with an appropriate variable name.
The directory class will be initialised/or have a constructor which accepts the directory path
The directory class will contain a method/function called scan directory that will return the list of file objects in
directory initialised by the path above. With the file objects properties/variables being filled with the
number of lines, spaces, characters words etc.

https://foothillcollege.instructure.com/courses/1916/assignments/26962
"""