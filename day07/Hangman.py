from Hangman_Art import stages, logo3, logo2
from Hangman_words import word_list
import random

game_over = False
lives = 6

chosen_word = random.choice(word_list)
correct_letters = []
letters_guessed = []

print(logo3)

while(not game_over):
    guess = input("\nGuess a letter: ").lower()
    display = ""
    for i in chosen_word:
        if(i == guess):
            display += i
            correct_letters.append(guess)
            letters_guessed.append(guess)
        elif(i in correct_letters):
            display += i
        else:
            display += '_'

    if("_" not in display):
        game_over = True
        print(logo2)
    if(guess not in chosen_word):
        lives -= 1
        letters_guessed.append(guess)
        print(stages[lives])
        print(f"Wrong! -1 to life.\nYou now have {lives} lives left\n")
        print(f"So far you have guessed these letters: {letters_guessed}")
    if(lives == 0):
        game_over = True
        print("You have run out of lives\nYou Lose!\n")
        print(f"The word was {chosen_word}")

    print(f"\nWord: {display}\n")
  








