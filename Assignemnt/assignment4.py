"""
Objectives:
Use a loop to read user input
Find an efficient algorithm
Material from:
Horstmann Chapter 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a program that reads a sequence of integer inputs (data) from the user and then prints the following results:

the total of all the inputs
the smallest of the inputs
the largest of the inputs
the number of even inputs
the number of odd inputs
the average of all of the inputs
You do not know how many numbers the user will want to type in, so you must ask her each time if she has another number
to add to the sequence.

There is no reason to store all of the user input in variables; it is far more efficient to store only the current
number that the user just typed in, along with the number that is the largest so far, the smallest so far, the total of
all typed in so far, etc.

The fastest way to complete this program is :

- Start by writing a program that satisfies just the first of the requirements.
- Test that program thoroughly. Then modify the program so that it satisfies just the first and second  requirements.
- Next modify the program so that it satisfies just the first, second and third requirements.

Continue to add functionality incrementally and test until you have a single program (and a single loop) that satisfies
all six requirements.


**********************************8
In Order to Receive Full Credit:
**********************************

Follow the specifications above EXACTLY. If you have questions, ask!
Adhere to the program guidelines that you will find in the Introduction Module here in Canvas.
Make sure that your prompts and messages use correct spelling and grammar.

Test your user interface by asking a friend to run your program and see if it is clear to her what she is supposed to do.

After running your program, copy and paste the contents of the Python Console in the same way you did in assignment #1.

You need to submit only the file containing your Python source code and a a paste of the Python Console showing what
happens when you run it.

document your code please :)

Here is a sample run, with user input in yellow:
This program will calculate statistics for your integer data.
Please type a number: 7
Do you have another number to enter? Y
Please type a number: -13
Do you have another number to enter? Y
Please type a number: -3
Do you have another number to enter? Y
Please type a number: 99
Do you have another number to enter? N

The total of your numbers is: 90
The smallest of your numbers is: -13
The largest of your numbers is: 99
The number of even numbers is: 0
The number of odd numbers is: 4
The average of your numbers is: 22.5


2. In class we saw the maximum of a list formulated recursively now write a function that recursively does the minimum.

Hint: some operations just need to be reversed and now use the largest integer possible is given by: sys.maxsize
"""

