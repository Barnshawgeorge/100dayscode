from art import *
import random

lives = 0
game_over = False
num_to_guess = random.randrange(1, 101)

def check_number(num):
    global lives
    global game_over
    if(num == num_to_guess):
        game_over = True
        print(f"You got it! The number was {num_to_guess}")
    elif(num > num_to_guess):
        lives -= 1
        print("Too High!")
    elif(num < num_to_guess):
        lives -= 1
        print("Too Low!")

def get_lives():
    print(f"You have {lives} attempts to guess the number.")

def lose():
    if(lives == 0):
        print(f"You are out of lives. The number to guess was {num_to_guess}")


print(logo)
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if(choose_difficulty == "easy"):
    lives = 10
    while(not game_over):
        get_lives()
        user_guess = int(input("Make a guess: "))
        check_number(user_guess)
if(choose_difficulty == "hard"):
    lives = 5
    while(not game_over):
        get_lives()
        user_guess = int(input("Make a guess: "))
        check_number(user_guess)       