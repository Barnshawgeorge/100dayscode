from art import *
import random

print(logo)

game_over = False
keep_playing = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

def shuffle(deck):
    random.shuffle(deck)
    return deck

def get_cards(deck, hand, num_cards):
    for i in range(0, num_cards):
        card = random.choice(deck)
        hand.append(card)
    return hand

def get_card_total(hand):
    total = 0
    for card_value in hand:
        if(card_value == 11 and total > 21):
            total -= 10
        elif(card_value == 11 and total >= 11):
            total +=1
        else:
            total += card_value
    return total

def calculate_ace(hand):
    for card in hand:
        if(card == 11 and get_card_total(hand) >= 11):
            return get_card_total(hand) - 10
        
            


while(not game_over):
    welcome_prompt = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if(welcome_prompt == 'y'):
        shuffle(cards)
        print(f"Your cards: {get_cards(cards, user_cards, 2)}, current score: {get_card_total(user_cards)}")
        print(f"Dealers first card: {get_cards(cards, dealer_cards, 1)}")
        if(get_card_total(user_cards) == 21):
            print("BLACKJACK!! YOU WIN")
            game_over = True
        while(not keep_playing):
            user_response = input("Type 'y' to get another card, type 'n' to pass: ")
            if(user_response == 'y'):
                print(f"Your cards: {get_cards(cards, user_cards, 1)}, current score: {get_card_total(user_cards)}")
                if(get_card_total(user_cards) == 21):
                    game_over, keep_playing = True, True
                    print("BLACKJACK!! YOU WIN")
                if(get_card_total(user_cards) > 21):
                    game_over, keep_playing = True, True
                    print("BUSTED!! YOU LOSE")
            if(user_response == 'n'):
                game_over, keep_playing = True, True
                print(f"Your final hand: {user_cards}, final score: {get_card_total(user_cards)}")
                print(f"Dealers final hand: {get_cards(cards, dealer_cards, 1)}, final score: {get_card_total(dealer_cards)}")
                if(get_card_total(dealer_cards) > get_card_total(user_cards)):
                    print("Dealer Wins")
                elif(get_card_total(dealer_cards) == get_card_total(user_cards)):
                    print("Tie. Try again")
                elif(get_card_total(user_cards) > get_card_total(dealer_cards)):
                    print("YOU WIN")




