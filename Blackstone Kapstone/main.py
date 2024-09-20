from art import logo
import os
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        card.remove(11)
        card.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose😤"
    elif user_score == computer_score:
        return "Draw☹️"
    elif computer_score == 0:
        return "Lose, opponent has blackjack☹️"
    elif user_score == 0:
        return "Win with a blackjack😎"
    elif user_score > 21:
        return "You went over, You lose☹️"
    elif computer_score > 21:
        return "Opponent went over, You win😁"
    elif user_score > computer_score:
        return "You Win 😃"
    else:
        return "you lose 😤"


def play_game():
    print(logo)

    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your card:{user_card}, current_score:{user_score}")
        print(f"Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("type 'y' to get anathor card, type 'n'to pass: ")
            user_should_deal = user_deal.lower
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f" Your final hand:{user_card}, final_score:{user_score}")
    print(f"computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()