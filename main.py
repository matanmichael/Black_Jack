import random
from art import logo
user_cards = []
computer_cards = []

def deal_card():
    """Deal cards to user and computer from a list of cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    """ Calculate the cards return 0 if player has blackjack and replace 11 with 1 """
    if sum(cards) == 21:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compareHands(user_score, computer_score):
        """Compare user's hands against computer's hands"""
        if user_score > 21 and computer_score > 21:
            return "You went over, you lose!"
        elif user_score > 21:
            return "You went over. You lose!"
        elif computer_score > 21:
            return "Computer went over, you won!"
        elif user_score == 0:
            return "Win with a Blackjack !"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack!"
        elif user_score == computer_score:
            return "Draw!"
        elif computer_score > user_score:
            return "You lost"
        elif computer_score < user_score:
            return "You Won"

def play_game():
    """"Starts the black jack game"""
    print(logo)
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_cards(user_cards)
    computer_score = calculate_cards(computer_cards)

    print(f"Your cards: {user_cards},current score: {sum(user_cards) }")
    print(f"Computer's first card: {computer_cards[0]} ")

    while not is_game_over :
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card())
                print(f"Your cards: {user_cards},current score: {sum(user_cards)}" )
                user_score = calculate_cards(user_cards)
            elif user_choice == 'n':
                is_game_over = True

    while computer_score != 0 and sum(computer_cards) < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_cards(computer_cards)
    print("")
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    print(compareHands(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    if __name__ == "__main__":
        user_cards.clear()
        computer_cards.clear()
        play_game()
