""" ASSIGNMENT 1

Student name : DAT NGUYEN
Course       : CS F003A -
Term         : Fall 2016 - Foothill College
Last Update  : 3:02 PM 10/5/2016

"""
# OUTPUT
# Connected to pyDev debugger (build 145.1504)
# Hello, World
# 234 * 456 =
# 106704
# Pi =  3.139592655589785
#
# Process finished with exit code 0



print("Hello, World")

# This prints the result of multiplying 234*456
print("234 * 456 =")
print(234*456)

# Problem 2: function that will output value of pi


def print_and_calculate_pi():
    sum_value = 0.0
    temp = 2                      # To set plus/minus sign
    for i in range(1, 1000, 2):

        sum_value += ((-1)**temp)/i
        temp += 1

    pi = sum_value*4
    return pi

print('Pi = ', print_and_calculate_pi())
