import random
from icons import *

computer_choice = random.randrange(0, 3)
icons = [rock, paper, scissors]

user_input = int(input("What do you you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(f"User chooses {icons[user_input]}\nComputer chooses {icons[computer_choice]}")

if(int(user_input) > 3):
    print("Not valid choice, please try again")
if((user_input == 0 and computer_choice == 2) or (user_input == 1 and computer_choice == 0) or (user_input == 2 and computer_choice == 1)):
    print("You win!")
if((user_input == 2 and computer_choice == 0) or (user_input == 0 and computer_choice == 1) or (user_input == 1 and computer_choice == 2)):
    print("You Lose!")
if(user_input == computer_choice):
    print("Tie")
