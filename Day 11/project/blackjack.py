import os
import random
from ui import logo
def deal_card():
    """Returns a Random Card Value from the Deck"""
    card_val = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_val)
    return card

def calculate_score(crd_lst):
    score = sum(crd_lst)
    if 11 in crd_lst and score > 21:
        crd_lst.remove(11)
        crd_lst.append(1)
    
    if score == 21 and len(crd_lst) == 2:
        return 0
    return score

def compare(user, comp):
    if user > 21 and comp > 21:
        return "You went over. You lose 😤"
    if user == comp:
        return "Draw 🙃"
    elif comp == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user == 0:
        return "Win with a Blackjack 😎"
    elif user > 21:
        return "You went over. You lose 😭"
    elif comp > 21:
        return "Opponent went over. You win 😁"
    elif user > comp:
        return "You win 😃"
    else:
        return "You lose 😤"

def main():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # sys.exit()
    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
            print ("The Game is Over")
        else:

            draw = input("Do you want to draw another card (type 'y' for yes and 'n' for no)").lower()
            if draw == 'y':
                user_cards.append(deal_card())
            elif draw == 'n':
                game_over = True
                print("The Game has ended")
        while comp_score != 0 and comp_score < 17:
            computer_cards.append(deal_card())
            comp_score = calculate_score(computer_cards)
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {comp_score}")
        print(compare(user_score, comp_score))

    reitr = input("Do you want to Play Again ?? \n (y to restart) : ").lower()
    while reitr == 'y':
        os.system('CLS')
        os.system('clear')
        main()
main()
