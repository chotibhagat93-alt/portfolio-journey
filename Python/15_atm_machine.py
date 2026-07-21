"""
Author: Sakshi Bhagat
Project: ATM Machine
"""

balance = 10000

print("====== ATM Machine ======")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your Balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit Successful")
    print("New Balance:", balance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")