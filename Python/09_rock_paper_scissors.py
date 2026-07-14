"""
Author: Sakshi Bhagat
Project: Rock Paper Scissors
"""

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper or scissors: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("🤝 It's a Tie!")

elif user == "rock" and computer == "scissors":
    print("🎉 You Win!")

elif user == "paper" and computer == "rock":
    print("🎉 You Win!")

elif user == "scissors" and computer == "paper":
    print("🎉 You Win!")

elif user not in choices:
    print("❌ Invalid Choice!")

else:
    print("💻 Computer Wins!")