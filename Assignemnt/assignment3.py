# Assignment 3
# Author : Dat Nguyen
# Date   : 10/13/2016
# Course : CS F003A - OO Methodologies in Python


# *****************************
# TEST CASE : Valid Input
# *****************************
# Enter driver age:  35
# Enter number of tickets: 1
# Enter car value: 10000
# Premium: $: $550.00
#
# --------------------------------------------------------------------------------
# Problem 2 - Number of last names matched the requirement is : 10638 lines.

# *****************************
# TEST CASE : Invalid Input
# *****************************
# Enter driver age:  21a
# Enter number of tickets: ?
# Enter car value: 50000
# Premium: $: $ 0.00

# *****************************
# TEST CASE : AGE IS < 16
# *****************************
# Enter driver age:  1
# Enter number of tickets: 2
# Enter car value: 2000
#
# Sorry, we cannot offer this driver insurance because he/she is too young.


# TEST CASE: HAVING TOO MANY TICKETS
# ---------------------------
# Car Insurance Premium Quote
# ---------------------------
# Enter driver age:  16
# Enter number of tickets: 5
# Enter car value: 10000
#
# Sorry, we cannot offer this driver insurance because he/she got too many tickets.

import re

"""


Use the following rules to calculate the premium:
The base premium is 5 percent of the value of the car. u
Drivers under 25 years old pay 15 percent more
Drivers from 25 through 29 pay 10 percent more.

A driver with
One traffic ticket pays 10 percent over the premium already figured.
Two tickets draws a     25 percent extra charge;
three tickets adds      50 percent;
Drivers with more than three tickets are refused coverage.

This is what the Python Run pane will look like when you run your program four times. Please use these test values when
 you create the recording of the run that you will turn in:

       Driver’s Age? 35
       Number of Tickets? 1
       Value of Car? 10000
       Premium: $550.00

       Driver’s Age? 29
       Number of Tickets? 2
       Value of Car? 15000
       Premium: $1031.25

       Driver’s Age? 19
       Number of Tickets? 3
       Value of Car? 850
       Premium: $73.31

       Driver’s Age? 81
       Number of Tickets?
       Value of Car? 12500
       Premium: $0

Notice the resulting premiums that your program must calculate and output given these specific inputs. But also note
that your program is required to work in other cases too, so it is your responsibility to test other input values to
ensure that your program works in all reasonable cases. You can assume that the user will only type in numbers.

In Order to Receive Full Credit:
•  To calculate the premium, first apply the base rate of 5% * value of the car to get the base premium, and then add a
 percentage of that premium for the age of the driver. Finally add a percentage of that premium for the number of
 tickets (if necessary). For example, for the driver age 19:

      Premium = (850 * .05)* 1.15 * 1.50 = 73.3125
                    ^                ^        ^
                    car value        age    tickets

•  Structure the conditions so that you have NO code duplication.

•  Try out other test cases to make sure that your program works for other common data as well.
You can assume that the user's input will all be positive numbers.

•  Don't forget to submit a recording of the run of your program as you did in the previous assignments.

"""


class DrivingRecord:
    driver_age = 0
    number_of_tickets = 0

    def __init__(self, age, tickets):
        self.driver_age = age
        self.number_of_tickets = tickets

    def get_driver_age(self):
        return self.driver_age

    def get_num_tickets(self):
        return self.number_of_tickets


def get_quote(record, car_value):

    # Validation
    # Age and Number of tickets should only be digit
    if not string_validation(record.get_driver_age(), '^[\d]+'):   #
        return -4
    if not string_validation(record.get_num_tickets(), '^[\d]+'):
        return -3

    premium = 0
    age_multiplier = 0
    driver_age = int(record.get_driver_age())
    driver_tickets = int(record.get_num_tickets())

    if driver_age < 16:
        return -2
    elif 16 < driver_age < 25:
        age_multiplier = 1.15
    elif 25 <= driver_age < 29:
        age_multiplier = 1.10
    else:
        age_multiplier = 1.0

    premium = (int(car_value)*0.05)*age_multiplier

    if driver_tickets == 1:
        premium += premium*0.10
    elif driver_tickets == 2:
        premium += premium*0.10
        premium += premium*0.25
    elif driver_tickets == 3:
        premium += premium * 0.10
        premium += premium * 0.50
    elif driver_tickets >= 4:
        return -1

    # These two variables might be implemented in real world situation, not in this scope of this exercise
    discount_multiplier = 1.0
    cash_discount = 0.0
    # Calculate premium
    premium = premium*discount_multiplier - cash_discount
    return premium


def string_validation(string, regex_pattern):
    pattern = re.compile(regex_pattern)
    return bool(pattern.search(string))

print("---------------------------")
print("Car Insurance Premium Quote")
print("---------------------------\n")

age = input("Enter driver age:  ")
tickets = input("Enter number of tickets: ")
car_value = input("Enter car value: ")

record = DrivingRecord(age, tickets)
quote = get_quote(record, car_value)
if quote == -1:
    print("\nWSorry, we cannot offer this driver insurance because he/she got too many tickets.")
elif quote == -2:
    print("\nSorry, we cannot offer this driver insurance because he/she is too young.")
elif quote == -3 or quote == -4:
    print('{:10}: ${:5.2f}'.format("Premium ", 0))
    print("\nInvalid input")
else:
    print('{:10}: ${:5.2f}'.format("Premium ", quote))


"""

2.  From the file CSV_Database_of_Last_Names.csvPreview the documentView in a new window , count the number of
Last Names ignoring the first letter, that have an "a" followed by any number of characters including 0 and the
followed by an  "e" followed by 1 or more characters.
"""
file = open('CSV_Database_of_Last_Names.csv', 'r')
lines = []

for l in file:
    lines.append(l)

# (^[\w]{1}a.*e.+) - 7061   (.a.*e.+) - 10638
pattern1 = re.compile("(.a.*e.+)")


def match_pattern(ls, pattern):
    l = pattern.findall(ls)
    if len(l) == 0:
        return False
    else:
      # Unit test:
      # print(l)
        return True

num_lines = sum([1 for l in lines if match_pattern(l, pattern1)])
print('\n\n--------------------------------------------------------------------------------')
print("Problem 2 - Number of last names matched the requirement is :", num_lines, "lines.")
file.close()
