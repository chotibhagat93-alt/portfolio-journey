"""
Author: Sakshi Bhagat
Topic: Grade Calculator
"""

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")

elif marks >= 75:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

elif marks >= 40:
    print("Grade: C")

elif marks >= 0:
    print("Fail")

else:
    print("Invalid Marks")