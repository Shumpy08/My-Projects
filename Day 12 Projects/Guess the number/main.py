import os
from random import randint

clear = lambda: os.system('cls')
EASY = 10
HARD = 5


def logo():
    LOGO = '''

    $$$$$$\                                                                                           $$\                         
    $$  __$$\                                                                                          $$ |                        
    $$ /  \__$$\   $$\ $$$$$$\  $$$$$$$\ $$$$$$$\        $$$$$$\        $$$$$$$\ $$\   $$\$$$$$$\$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\  
    $$ |$$$$\$$ |  $$ $$  __$$\$$  _____$$  _____|       \____$$\       $$  __$$\$$ |  $$ $$  _$$  _$$\$$  __$$\$$  __$$\$$  __$$\ 
    $$ |\_$$ $$ |  $$ $$$$$$$$ \$$$$$$\ \$$$$$$\         $$$$$$$ |      $$ |  $$ $$ |  $$ $$ / $$ / $$ $$ |  $$ $$$$$$$$ $$ |  \__|
    $$ |  $$ $$ |  $$ $$   ____|\____$$\ \____$$\       $$  __$$ |      $$ |  $$ $$ |  $$ $$ | $$ | $$ $$ |  $$ $$   ____$$ |      
    \$$$$$$  \$$$$$$  \$$$$$$$\$$$$$$$  $$$$$$$  |      \$$$$$$$ |      $$ |  $$ \$$$$$$  $$ | $$ | $$ $$$$$$$  \$$$$$$$\$$ |      
    \______/ \______/ \_______\_______/\_______/        \_______|      \__|  \__|\______/\__| \__| \__\_______/ \_______\__|      




    '''
    print(LOGO)


def check(answer, guess, turns):
    '''Checks the game'''
    if answer > guess:
        print("Too Low")
        return turns - 1
    elif answer < guess:
        print("Too High")
        return turns - 1
    else:
        print(f"Nice! You got it. The right number was {answer}")


def level():
    level = input("Type 'easy' for 10 attempts and 'hard' for 5 attempts: ").lower()
    if level == "easy":
        return EASY
    elif level == "hard":
        return HARD


def game():
    '''Guess a Number Game'''
    logo()
    print("WELCOME TO GUESS THE NUMBER GAME PROJECT BY SHUMPY.")
    print("I'm thinking of a number from 1 to 100.")
    answer = randint(1, 100)
    turns = level()
    print(f"You have {turns} attempts to get the right number.")
    print(f"Psst the right number is {answer}. [FOR TESTING PURPOSE]")
    guess = 0
    while answer != guess:
        guess = int(input("Make a guess: "))
        turns = check(answer, guess, turns)
        if answer != guess:
            print(f"You have {turns} attempts left")
        if turns == 0:
            print(f"You lose. You have 0 attempts left.")
            return
        elif answer != guess:
            print("Guess again")


clear()
end = True
while end:
    ask = input("Do you want to play the game of Guess the Number? Type 'yes' or 'no': ").lower()
    if ask == "yes":
        clear()
        game()
    else:
        clear()
        end = False
        print("Thanks! Have a Nice Day >_<")
