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


def string_validation(string, regex_pattern):
    pattern = re.compile(regex_pattern)
    return bool(pattern.search(string))


def get_quote(record, car_value):

    # Validation
    # Age and Number of tickets should only be digit
    if not string_validation(record.get_driver_age(), '^[\d]+'):   #
        return -4
    if not string_validation(record.get_num_tickets(), '^[\d]+'):
        return -3

    premium = 0
    age_multiplier = 0
    ticket_multiplier = 0
    driver_age = int(record.get_driver_age())
    driver_tickets = int(record.get_num_tickets())

    if driver_age < 16:
        return -2
    elif 16 < driver_age < 25:
        age_multiplier = 1.15
    elif 25 <= driver_age <= 29:
        age_multiplier = 1.10
    else:
        age_multiplier = 1.0

    if driver_tickets == 1:
        ticket_multiplier = 1.10
    elif driver_tickets == 2:
        ticket_multiplier = 1.25
    elif driver_tickets == 3:
        ticket_multiplier = 1.50
    elif driver_tickets >= 4:
        return -1

    # Calculate premium
    premium = (int(car_value)*0.05)*age_multiplier*ticket_multiplier
    return premium

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
        # print(l)
        return True

num_lines = sum([1 for l in lines if match_pattern(l, pattern1)])
print('\n\n--------------------------------------------------------------------------------')
print("Problem 2 - Number of last names matched the requirement is :", num_lines, "lines.")
file.close()
