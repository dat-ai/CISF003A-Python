""" ASSIGNMENT 2  - The Cost of Driving

Student name : DAT NGUYEN
Course       : CS F003A - OO Methodologies in Python
Term         : Fall 2016 - Foothill College
Last Update  : 3:02 PM 10/5/2016

"""
import math
# PRO Calculate how far car can drive with current gas_level


def remaining_distance(current_gas_level, mpg):
    return float(mpg)*float(current_gas_level)


def cost_for_100_miles(mpg, price):
    required_gas = 100.0 / float(mpg)
    total_cost = required_gas * float(price)
    return total_cost


print("---------------------------")
print("Cost of Driving Calculator")
print("---------------------------\n")

car_mpg = input("Please enter your car's MPG (mile per gallon):  ")
gas_price = input("Please enter the price of gas per gallon: ")
car_gas_tank_level = input("Please enter the number of gallons of gas currently in your car's gas tank: ")


print('\n{:25} : ${:5.2f}'.format("Cost of driving 100 miles", cost_for_100_miles(car_mpg, gas_price)))
print('{:25} :{:5} miles'.format("Remaining distance", remaining_distance(car_gas_tank_level, car_mpg)))


# =============== PROBLEM 2 ========================


def is_odd(n):
    return n % 2 == 1


def is_perfect_squared(n):
    return math.sqrt(n)**2 == n


def special_sum(a_list):
    return sum([i**2 for i in a_list] + [i for i in a_list if is_odd(i) or is_perfect_squared(i)])

print("\nThe sum of perfect squared numbers/odd numbers/all double number in a list [1,1000] is : "
      , special_sum(range(1, 1001)))


# OUTPUT CONSOLE
# ---------------------------
# Cost of Driving Calculator
# ---------------------------
#
# Please enter your car's MPG (mile per gallon):  21
# Please enter the price of gas per gallon: 3
# Please enter the number of gallons of gas currently in your car's gas tank: 2
#
# Cost of driving 100 miles : $14.29
# Remaining distance        : 42.0 miles
#
# The sum of perfect squared numbers/odd numbers/all double number in a list [1,1000] is :  334218814
#
# Process finished with exit code 0

