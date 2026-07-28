"""
Author: Sakshi Bhagat
Project: Contact Book
"""

contacts = []

print("===== CONTACT BOOK =====")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("Enter Contact Name: ")
    contacts.append(name)
    print("Contact Added Successfully!")

elif choice == 2:
    print("Saved Contacts")
    for contact in contacts:
        print(contact)

elif choice == 3:
    search = input("Enter Contact Name: ")

    if search in contacts:
        print("Contact Found")
    else:
        print("Contact Not Found")

elif choice == 4:
    print("Thank You!")

else:
    print("Invalid Choice")