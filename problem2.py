#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
import math


integer1 = int(input("Enter a number: "))
integer2 = int(input("Enter another number: "))

if integer1 >= integer2 and integer1 % integer2 == 0:
    print(f"{integer1} is a factor of {integer2}")

elif integer1 >= integer2 and integer1 % integer2 >= 1:
    print(f"{integer1} is not a factor of {integer2}")

if integer2 >= integer1 and integer2 % integer1 == 0:
    print(f"{integer2} is a factor of {integer1}")

if integer1 >= integer2 and integer1 % integer2 >= 1:
    print(f"{integer1} is not a factor of {integer2}")



