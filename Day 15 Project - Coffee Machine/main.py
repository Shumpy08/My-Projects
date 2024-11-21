import os

from data import MENU, resources

clear = lambda: os.system('cls')

profit = 0


def is_resources_sufficient(items):
    '''checks if the resources to make coffee is sufficient or not'''
    for item in items:
        if items[item] > resources[item]:
            print(f"\nSorry, theres not enough {item} to make the coffee.")
            return False
    return True


def process_coins():
    '''Process Coins in the machine and gives change back to the customer'''
    print("Please Insert Coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(drink_cost, actual_cost):
    '''Checks if the transaction is successful or not'''
    if drink_cost >= actual_cost:
        change = round(drink_cost - actual_cost, 2)
        print(f"\nHere's your ${change} in change.")
        global profit
        profit += actual_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_items, drink_name):
    for item in order_items:
        resources[item] -= order_items[item]
    print(f"\nHere's your {drink_name}. Enjoy ☕")


should_continue = True
clear()
while should_continue:
    choice = input("\nWhat would you like? (espresso [$1.50]/ latte [$2.50]/ cappuccino [$3]): ").lower()
    if choice == "off":
        should_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink["ingredients"], choice)
