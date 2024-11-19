print('''Welcome to Life in Weeks and Days Calculator.\n''')
age = int(input("Enter your age: "))


def life_in_weeks():
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    days_remaining = years_remaining * 365
    print(f"You've {weeks_remaining} weeks or {days_remaining} days left.")
    print("Remember to not count the days, but to make the days count champ ❤.︎")


life_in_weeks()
