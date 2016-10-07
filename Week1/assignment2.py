""" ASSIGNMENT 2  - The Cost of Driving

Student name : DAT NGUYEN
Course       : CS F003A - OO Methodologies in Python
Term         : Fall 2016 - Foothill College
Last Update  : 3:02 PM 10/5/2016

"""
# Write a function that takes the list range(1,10000) and returns the
# sum of the elements that are perfect squares + the sum of the odd numbers + double every number.
# Remember a perfect square is a number whose square root is an integer.
# Calculate the cost of driving for 100 miles


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
print('{:25} :{:5} miles'.format("Remaining distance", remaining_distance(car_gas_tank_level, gas_price)))


# OUTPUT CONSOLE
# Connected to pyDev debugger (build 145.1504)
# ---------------------------
# Cost of Driving Calculator
# ---------------------------
#
# Please enter your car's MPG (mile per gallon):  25
# Please enter the price of gas per gallon: 2.43
# Please enter the number of gallons of gas currently in your car's gas tank: 10
#
# Cost of driving 100 miles : $ 9.72
# Remaining distance        : 24.3 miles
#
# Process finished with exit code 0



