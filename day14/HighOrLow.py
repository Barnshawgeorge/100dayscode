from art import logo, vs
from data import data
import random
import os

game_over = False
score = 0

def user_guess():
    guess = input("Who has more followers? Type 'A' or 'B': ")
    print()
    return guess

def compare(dict):
    global score
    global game_over
    choice_one = random.choice(dict)
    choice_two = random.choice(dict)
    print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}")
    print(vs)
    print(f"Compare B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']}")
    if(choice_one['follower_count'] > choice_two['follower_count'] and user_guess() == 'A'):
        os.system('clear')
        score += 1
        print(f"Correct! Current score: {score}")
    elif(choice_two['follower_count'] > choice_one['follower_count'] and user_guess() == 'B'):
        os.system('clear')
        score += 1
        print(f"Correct! Current score: {score}")
    else:
        print(f"Wrong! Game over, Final Score: {score}")
        game_over = True


while(not game_over):
    print(logo)
    compare(data)

    
    