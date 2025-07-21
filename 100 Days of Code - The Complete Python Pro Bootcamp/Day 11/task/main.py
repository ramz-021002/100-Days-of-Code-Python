import art
import random as random

def drawcard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def give_cards():
    print(art.logo)
    user_cards = [drawcard(), drawcard()]
    computer_cards = [drawcard(), drawcard()]
    current_sum_user = sum(user_cards)
    print(f"Your current cards: {user_cards}, current score = {current_sum_user}")
    print(f"Computer's first card: {computer_cards[0]}")
    return user_cards, computer_cards

def another_card(card):
    new_card = drawcard()
    card.append(new_card)
    return card

def winning(user_cards, computer_cards):
    user_total = sum(user_cards)
    computer_total = sum(computer_cards)
    print(f"Your final hand: {user_cards}, final score = {user_total}")
    print(f"Computer's final hand: {computer_cards}, final score = {computer_total}")
    if user_total == 21 and len(user_cards) == 2:
        print("You win. As Black Knight")
    elif computer_total == 21 and len(computer_cards) == 2:
        print("You loose")
    elif computer_total <= 21 and computer_total == user_total :
        print("It's a tie")
    elif user_cards > computer_cards and user_total <= 21:
        print("You won!!!!")
    elif user_cards < computer_cards and computer_total <= 21:
        print("You lose 😤")
    else:
        print("No Decision")

def start_game():
    computer_deck = []
    user_deck = []
    continue_game = True
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'y':
        user_deck, computer_deck = give_cards()
    else:
        print("Bye Bye")
        continue_game = False
    user_extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while continue_game:
        computer_extra_card = ''
        if user_extra_card == 'y':
            user_deck= another_card(user_deck)
            if sum(user_deck) > 21 and 11 in user_deck:
                user_deck.remove(11)
                user_deck.append(1)

            if sum(user_deck) > 21:
                winning(user_deck, computer_deck)
                continue_game = False
                start_game()
            else:
                print(f"Your current cards: {user_deck}, current score = {sum(user_deck)}")
                print(f"Computer's first card: {computer_deck[0]}")
        else:
            computer_extra_card = random.choice(['y', 'n'])

        if computer_extra_card == 'y':
            computer_deck = another_card(computer_deck)
            if sum(computer_deck) > 21 and 11 in computer_deck:
                computer_deck.remove(11)
                computer_deck.append(1)

            if sum(computer_deck) > 21:
                winning(user_deck, computer_deck)
                continue_game = False
                start_game()
        else:
            continue_game = False
            winning(user_deck, computer_deck)
            start_game()


start_game()