"""
Author: Sakshi Bhagat
Topic: Student Dictionary
"""

student = {}

student["name"] = input("Enter Name: ")
student["branch"] = input("Enter Branch: ")
student["cgpa"] = float(input("Enter CGPA: "))

print("\n----- Student Details -----")
print("Name   :", student["name"])
print("Branch :", student["branch"])
print("CGPA   :", student["cgpa"])