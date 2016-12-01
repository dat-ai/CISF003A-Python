
import re as regex
import collections
from os import listdir
from os.path import isfile, join

"""
OUTPUT
Please enter a filename (e.g.: /path/to/filename) : dat2
Invalid file name Please try again
Please enter a filename (e.g.: /path/to/filename) : dat2.txt
File dat2.txt is not found.
Please enter a filename (e.g.: /path/to/filename) : dat.txt

File report :dat.txt
w: 6.25%
i: 14.58%
v: 2.08%
e: 10.42%
g: 2.08%
h: 8.33%
r: 6.25%
d: 6.25%
n: 8.33%
t: 6.25%
f: 2.08%
c: 4.17%
l: 4.17%
s: 8.33%
a: 10.42%


------------------------------
DICTIONARY OBJECT
------------------------------
Please enter a file path (e.g.: /path/to/directory) : ./samples
Total files in ./samples: 3
File report :./samples/test3.txt
p: 3.37%
a: 8.99%
u: 5.62%
i: 10.11%
n: 4.49%
e: 8.99%
o: 4.49%
g: 2.25%
s: 7.87%
y: 2.25%
c: 3.37%
r: 8.99%
t: 10.11%
f: 1.12%
d: 1.12%
m: 2.25%
l: 7.87%
h: 3.37%
w: 3.37%

File report :./samples/test1.txt
w: 6.12%
i: 14.29%
v: 2.04%
e: 10.20%
g: 2.04%
h: 8.16%
r: 6.12%
d: 6.12%
n: 8.16%
t: 6.12%
f: 2.04%
c: 4.08%
l: 4.08%
s: 10.20%
a: 10.20%

File report :./samples/test2.txt
p: 2.03%
u: 5.08%
b: 1.02%
r: 8.12%
t: 11.68%
f: 1.52%
d: 3.05%
w: 2.54%
y: 1.02%
k: 0.51%
a: 6.09%
i: 5.08%
m: 2.03%
e: 14.21%
o: 4.57%
g: 2.03%
s: 4.57%
x: 0.51%
n: 11.17%
c: 2.03%
l: 5.58%
h: 5.58%


Process finished with exit code 0
"""


class FileStat:
    """
    This fileStat object will count the frequency of each letter in the file
    """
    def __init__(self, filename):
        self.file_name = filename
        self.char_counter = {}
        self.frequency_table = {}
        self.total_chars = 0

    def count(self):
        """
        Calculate the frequency of each letter in a file
        :return: a frequency table - dictionary
        """
        f = self.open_file(self.file_name)

        # Get all the chars in file
        self.total_chars = regex.findall(r'[a-zA-Z]', f.read().lower())
        # Calculate concurrences of each letter.
        self.char_counter = collections.Counter(self.total_chars)

        # Get frequency for each letter
        for k in self.char_counter:
            self.frequency_table[k] = self.char_counter[k]*100 / len(self.total_chars)

        f.close()

    def open_file(self, file_name):
        """
        Open file using provided filename
        :param file_name: a string contains path to file
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

    def __str__(self):
        """
        Display FileStat
        :return: a string
        """
        # Display frequency table
        output = "\nFile report :" + self.file_name + "\n"
        for k in self.frequency_table:
            output += '{:1}: {:3.2f}%'.format(k, self.frequency_table[k]) + "\n"
        return output


class DirectoryStat:
    """
    Keep track of each fileStat in a directory.
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
            a_file = FileStat(fl)
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

if __name__ == "__main__":

    file_name = get_file_name()
    freq_table = FileStat(file_name)
    freq_table.count()
    print(freq_table)

    print("\n------------------------------")
    print("DICTIONARY OBJECT")
    print("------------------------------")
    test_path = get_path_name()
    directory_object = DirectoryStat(test_path)
    directory_object.count()
    print(str(directory_object))


"""
# Objectives:
Read a data file and analyze its contents
Use a Python dictionary to store counters
Material from:
Horstmann Chapter 8, or
Zyante ebook Chapter 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linguists find it interesting to see how often certain letters of the alphabet are used by various authors and in
different languages. For this assignment you will write a program that calculates the frequency of all the letters
(a through z) in a file specified by the user.

For this assignment your program will ask the user for the name of a file, open the file and read it through once.
Your program will then report on the frequency of each letter of the alphabet, regardless of case (capital or lower case)
. Recall that the frequency of a letter is defined to be the number of times that letter appears in the file divided by
the total number of letters in the file.

Please submit your source code file, a sample data file and a recording of the run your program generates when it
processes the sample data file.

Hints:
Reuse the function you wrote for Assignment #7 that repeatedly asks the user for the name of a file until your program
is able to open the file.
Create various data files to test your program with. For example, you can create a file with just "a"s and "A"s and
 white space and punctuation marks in it to see that the frequency of "a" is output as 100% and the frequency of
 all the rest of the letters is output as 0%.

The string methods built into Python will be helpful for this assignment also:
https://docs.python.org/3.1/library/stdtypes.html#string-methods (Links to an external site.)

In order to receive full credit:
Reuse the function you wrote for Assignment #7 that reads the filename and opens the file.
Use a dictionary to keep track of the count of each letter of the alphabet.
Read through the file just once in order to compile all of the required statistics
Use a classes and object oriented programming for this
And then use this class to do this for all the files in a folder as in assignment 7
"""