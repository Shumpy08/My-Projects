import os
import random

clear = lambda: os.system('cls')


print("Rock Paper Scissors Game")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
user = int(input("\nType 0 for Rock, 1 for Paper and 2 for Scissors: "))
user_choice = game[user]
print("\nYou chose:")
print(user_choice)
computer = random.randint(0, 2)
comp_choice = game[computer]
print(f"Computer chose:\n"
      f"{game[computer]}")

if user_choice == rock and comp_choice == paper:
    print("You chose rock while computer chose paper\nYou Lose")
elif user_choice == rock and comp_choice == scissors:
    print("You chose rock while computer chose Scissors\nYou Win")
elif user_choice == paper and comp_choice == rock:
    print("You chose Paper while computer chose Rock\nYou Win")
elif user_choice == paper and comp_choice == scissors:
    print("You chose Paper while computer chose Scissors\nYou Lose")
elif user_choice == scissors and comp_choice == rock:
    print("You chose Scissors while computer chose Rock\nYou Lose")
elif user_choice == scissors and comp_choice == paper:
    print("You chose Scissors while computer chose Paper\nYou Win")
elif user_choice == comp_choice:
    print("You and computer both choose same input\nIt's a Draw")
