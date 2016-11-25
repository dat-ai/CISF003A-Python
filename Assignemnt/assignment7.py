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

