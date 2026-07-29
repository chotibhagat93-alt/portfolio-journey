"""
Author: Sakshi Bhagat
Topic: Sum of Numbers
"""

number = int(input("Enter a number: "))

sum = 0
count = 1

while count <= number:
    sum = sum + count
    count = count + 1

print("Sum =", sum)