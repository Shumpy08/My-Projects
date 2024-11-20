logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(logo)
print("Welcome to Shumpy's Calculator.")


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def Calculator():
    num1 = float(input("Enter the number: "))
    for key in operators:
        print(key)
    end = True
    while end:
        choice = input("Choose an operator from above: ")
        num2 = float(input("Enter another number: "))
        calculation = operators[choice]
        answer = calculation(n1=num1, n2=num2)
        print(f"{num1} {choice} {num2} = {answer}")
        again = input("Type 'y' to continue and 'n' to start anew: ").lower()
        if again == "y":
            num1 = answer
        if again == "n":
            end = False
            Calculator()


Calculator()
