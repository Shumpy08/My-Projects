from art import logo, vs
from dictionary import data

import os
import random

clear = lambda: os.system('cls')


def check(guess, a, b):
    if a > b:
        return guess == 'a'
    else:
        return guess == "b"


def format(account):
    name = account["name"]
    des = account["description"]
    country = account["country"]
    return f"{name}, a {des} from {country}"


def random_accounts():
    return random.choice(data)


def game():
    clear()
    print(logo)
    acc_a = random_accounts()
    acc_b = random_accounts()
    score = 0
    should_continue = True
    while should_continue:
        acc_a = acc_b
        acc_b = random_accounts()
        while acc_a == acc_b:
            acc_b = random_accounts()
        print(f"Compare A: {format(acc_a)}")
        print(vs)
        print(f"Against B: {format(acc_b)}")

        follower_count_a = acc_a["follower_count"]
        follower_count_b = acc_b["follower_count"]
        guess = input("Who's got more followers? 'A' or 'B': ").lower()
        should_continue = check(guess, follower_count_a, follower_count_b)

        if should_continue:
            clear()
            print(logo)
            score += 1
            print(f"You got it right. Current score: {score}")
        else:
            should_continue = False
            clear()
            print(f"You lose. Total Score: {score}")


game()
