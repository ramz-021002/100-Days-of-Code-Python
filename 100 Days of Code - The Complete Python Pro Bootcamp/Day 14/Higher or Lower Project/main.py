import art
import game_data
import random as random

print(art.logo)
final_score=0

def pick_two_persons():
    first = random.choice(game_data.data)
    second = random.choice(game_data.data)
    if first == second:
        second = random.choice(game_data.data)
    return first, second

def game():
    global final_score
    correct = True
    handle_a, handle_b = pick_two_persons()
    while correct:
        print(f"Compare A: {handle_a['name']},a {handle_a['description']}, from {handle_a['country']}")
        print(art.vs)
        print(f"Against B: {handle_b['name']},a {handle_b['description']}, from {handle_b['country']}")
        user_input = input("Who has more followers? Type 'A' or 'B':").lower()
        if user_input == 'a' and handle_a['follower_count'] > handle_b['follower_count']:
            final_score += 1
            print(f"You're right! Current score: {final_score}")
            handle_a = handle_b
            _, handle_b = pick_two_persons()
        elif user_input == 'b' and handle_a['follower_count'] < handle_b['follower_count']:
            final_score += 1
            print(f"You're right! Current score: {final_score}")
            handle_a, handle_b = pick_two_persons()
        else:
            correct = False
            print(f"Sorry, that's wrong. Final score: {final_score}")

game()