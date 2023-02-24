import random
from os import system #for windows
from art import logo


clear = lambda: system('cls')
def final_hand(cards1, cards2, score1, score2):
    print(f"Your final hand: {cards1}, final score: {score1}")
    print(f"Computer's final hand: {cards2}, final score: {score2}")


def winner(score1, score2):
    if (score1 > 21 and score2 < 21) or (score1 < 21 and score2 < 21 and score2 > score1) or (score2 == 21):
        print("You went over. You lose.")
    elif score1 > 21 and score2 > 21 or score1 == score2:
        print("It's a draw!")
    elif (score1 < 21 and score2 > 21) or (score1 < 21 and score2 < 21 and score1 < score2) or (score1 == 21):
        print("You win.")


def blackjack():
    blackjack_question = input("Do you wanna play a game of BlackJack?Type 'y' or 'n': ")
    clear()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if blackjack_question == 'y':
        print(logo)
        your_cards = [random.choice(cards), random.choice(cards)]
        your_score = sum(your_cards)
        computer_cards = [random.choice(cards), random.choice(cards)]
        computer_score = sum(computer_cards)
        print(f"""
Your cards: {your_cards}, current score: {your_score}
Computer's first card: {computer_cards[0]}""")
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_continue == 'y':
            your_third_card = random.choice(cards)
            your_cards.append(your_third_card)
            your_score += your_third_card
        if computer_score < 17:
            computer_third_card = random.choice(cards)
            computer_cards.append(computer_third_card)
            computer_score += computer_third_card
        final_hand(your_cards, computer_cards, your_score, computer_score)
        winner(your_score, computer_score)
        blackjack()

blackjack()

