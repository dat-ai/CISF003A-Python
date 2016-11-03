"""
Objectives:
Use functions that were written by someone else to solve a problem
Define your own function that takes a parameter and returns a value
Test your program thoroughly
Material from:
Horstmann Chapter 5, or 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a function that takes:
 - a whole number as parameter
 - returns a string containing the number spelled out in English.
For example, the function call:  spell (123123)
will return the string:          "one hundred twenty three thousand one hundred twenty three"

Your function must work for any whole number whose value is between -999,999,999 and 999,999,999.
Of course, the numbers will not have commas in Python.

I have provided you with four function definitions that will help you in defining function spell().
You will find these function definitions in a source code file herePreview the documentView in a new window.
Start by becoming familiar with what these four functions do. Read the comment for each function.
Write a test program that calls each of these four functions and prints their returned values.
Do not modify any of these functions in any way.
Finally, you can read the full definition for each of these given functions if you want to, though that is certainly not
necessary in order to use them effectively.

Once you thoroughly understand how to call each of those four functions and what they will return,
it is time to write your own function definition for function spell().
The definition for function spell() that you write will be inside the same source code file as the other given function definitions.
More importantly, the definition for function spell() that you write will call these other functions either directly or indirectly.

The trick to defining your own function is to always write the test program first, before you try to write the definition itself. Here is a sample test program for your function spell():
     print (spell (123456789) )
     print (spell (456678) )
     print (spell (66) )
     print (spell (-123456789) )
     print (spell (-456678) )
     print (spell (-418) )
     print (spell (-13456678) )
Before you can start writing the definition for function spell(), you need to be able to write down:

"what output you want this program to generate when you are finished with this assignment".

You might find this website useful in telling what the returned values from your spell() function should look like:

Also, the use of the word "and" and the additional commas that this website
includes are not necessary for your function to generate.

In order to receive full credit:
Your program (which includes at least five function definitions) can have no duplicate code;
the names of the numbers must appear only once in your whole source code file.

The function you define must be named "spell"
The function you define must have a comment telling what the function does with its parameter(s) and what (if anything) it returns.
Your function spell() must not do any printing.
You must not modify the functions I gave you in any way
"""

MAX_RANGE = 999999999
MIN_RANGE = -999999999

# Reference: How to Spell Number in English
# http://www.grammarbook.com/numbers/numbers.asp
# Initialize base
dict_base = {0:"",1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
             11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
             19: "nineteen"}
dict_100th = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
              70: "seventy", 80: "eighty", 90: "ninety"}


def spell(whole_num: int):
    """
    This function will spell out a given number
    :param whole_num: a whole number ( could be negative/positive)
    :return: a string spelling that number

    e.g:
             spell(120365):
                            "one hundred thousand three hundred sixty five"
             spell(-623,456,789)
                            "negative six hundred twenty three millions four hundred fifty six seven eighty nine

    """
    remaining = abs(whole_num)
    str_result = ""
    if whole_num < 0:
        str_result = "Negative"
    prev_remainder = 0
    base_seed = 100                             # seeder to separate number
    while remaining > 0:
        print("\n\nPrevious remainder: " + str(prev_remainder))
        curr_remainder = remaining % base_seed
        remaining -= curr_remainder
        if base_seed == 100:
            str_result += base(curr_remainder)

        print("Current remainder:" + str(curr_remainder) + " " + str_result)
        base_seed *= 10
        prev_remainder += curr_remainder

    return "sample " + str(whole_num)


def base(remainder):
    """
    Helper function of spell() to call the one  <100th part

    :param remainder: a  number to spell
    :return: a string which spells out the number
    e.g : 12 : "twelve"
          23 : "twenty-three"
    """
    if remainder < 20:
        return dict_base[remainder]
    else:
        # determine the "---ty" part e.g (twenty, forty, fifty)
        ty_part = 10 * int(remainder / 10)
        str_result = dict_100th[ty_part]
        # determine the remaining part
        str_result += "-" + dict_base[remainder % 10]
        return str_result


def thousand(remainder):
    """
    Helper function to spell the thousand part
    :param remainder: a number
    :return: a string
    """

# main function
if __name__ == "__main__":
    print("------------------------------")
    print("SIMPLE NUMBER SPELLING PROGRAM")
    print("------------------------------")
    run = True
    while run:
        num = input("Enter a whole number (or enter 'x' to exit): ")
        try:                                            # try to convert input into integer
            num = int(num)
        except ValueError:
            if num == 'x':                              # if user enters 'x'
                break                                   # Exit the program
            else:                                       # Else, notify that input is invalid
                print("\nInvalid input(number only). Try again\n")
                continue
        if not (MIN_RANGE <= num <= MAX_RANGE):
            print("\nInput is out of range ( -999,999,999 to 999,999,999). Please try again\n")
            continue

        # spell will convert 'num' into a string by spelling it.
        result = spell(num)
        print(result)




