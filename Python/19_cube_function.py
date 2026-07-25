"""
Author: Sakshi Bhagat
Topic: Cube Function
"""

def cube(number):
    return number * number * number

num = int(input("Enter a number: "))

result = cube(num)

print("Cube =", result)