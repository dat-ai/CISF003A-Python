# Assignment 3
# Author : Dat Nguyen
# Date   : 10/13/2016
# Course : CS F003A - OO Methodologies in Python

import re
class DrivingRecord:
    driver_age = 0
    number_of_tickets = 0

    def __init__(self, age, tickets):
        self.driver_age = int(age)
        self.number_of_tickets = int(tickets)

    def getDriverAge(self):
        return self.driver_age

    def getNumberOfTickets(self):
        return self.number_of_tickets


def getQuote(record, car_value):

    premium = 0
    premium_multiplier = 0.05
    discount_multiplier = 1.0
    cash_discount = 0.0
    age = record.getDriverAge()
    tickets = record.getNumberOfTickets()

    if age < 16:
        return -2
    elif 16 < age < 25:
        premium_multiplier = 0.15
    elif 25 <= age <= 29:
        premium_multiplier = 0.10

    if tickets == 1:
        premium_multiplier += 0.10
    elif tickets == 2:
        premium_multiplier += 0.25
    elif tickets == 3:
        premium_multiplier += 0.50
    elif tickets >= 4:
        return -1

    premium = (int(car_value)*premium_multiplier)*discount_multiplier - cash_discount
    return premium


print("---------------------------")
print("Car Insurance Premium Quote")
print("---------------------------\n")

age = input("Enter driver age:  ")
tickets = input("Enter number of tickets: ")
car_value = input("Enter car value: ")

record = DrivingRecord(age, tickets)
quote = getQuote(record, car_value)
if quote == -1:
    print("\nWe cannot offer this driver insurance because he/she got too many tickets.")
elif quote == -2:
    print("\nWe cannot offer this driver insurance because he/she is too young.")
else:
    print("\n\nPremium for this driver is : $", quote)


"""
Assignment #3: "Branching Out"
 Submit Assignment
Due Tuesday by 11:59pm  Points 5  Submitting a file upload  File Types py
Objectives:
Use if, if/else, and elif
Factor out repetitive statements
Material from: Chapter 3,
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HiRisq Insurance company determines auto insurance rates based on a driver’s age, number of tickets in the last
three years, and the value of the car. Write a program that prompts the user for the required information, reads in
her responses, and calculates and prints the monthly premium that this driver will have to pay for insurance.

The information that the user is required to type in is: value of car, age of driver, number of traffic tickets.
The information that your program must calculate and print back out is just the monthly premium that this driver must
pay for insurance.

Use the following rules to calculate the premium:
The base premium is 5 percent of the value of the car. u
Drivers under 25 years old pay 15 percent more
Drivers from 25 through 29 pay 10 percent more.

A driver with one traffic ticket pays 10 percent over the premium already figured.
Two tickets draws a 25 percent extra charge;
three tickets adds 50 percent;
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
       Number of Tickets? 4
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



2.  From the file CSV_Database_of_Last_Names.csvPreview the documentView in a new window , count the number of
Last Names ignoring the first letter, that have an "a" followed by any number of characters including 0 and the
followed by an  "e" followed by 1 or more characters.
"""
file = open('CSV_Database_of_Last_Names.csv', 'r')
lines = []

for l in file:
    lines.append(l)

patt = re.compile("(.a.*e.+)")  # (^[\w]{1}a.*e.+) - 7061   (.a.*e.+) - 10638


def match_pattern(ls, pattern):
    l = pattern.findall(ls)
    if len(l) == 0:
        return False
    else:
      #  print(l)
        return True

num_lines = sum([1 for l in lines if match_pattern(l, patt)])
print("\n\nProblem 2 - Number of last names matched the required:", num_lines, "lines.")
file.close()
