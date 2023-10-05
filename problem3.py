#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

number1 = int(input("enter a number: "))
number2 = int(input("enter a second number: "))
number3 = int(input("enter a third number: "))

if number1 >= number2 and number1 >= number3:
    print(f"{number1}\n{number2}\n{number3}")

elif number2 >= number1 and number2 >= number3:
    print(f"{number2}\n{number1}\n{number3}")

elif number3 >= number1 and number3 >= number2:
    print(f"{number3}\n{number2}\n{number1}")


