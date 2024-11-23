import json
from random import shuffle, choice, randint
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:
            {
                "email": email,
                "password": password,
            }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message='Please make sure you dont leave any fields empty')
    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website.upper(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="'Error", message=f"Credentials  For {website.title()} Does Not Exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Shumpy's Password Manager")
window.config(pady=50, padx=50)

my_pass = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=my_pass)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)
email_input = Entry(width=39)
email_input.insert(0, "Pucei379@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate = Button(text="Generate password", command=generate_password)
generate.grid(column=2, row=3)

search = Button(text="Search", width=13, command=find_password)
search.grid(column=2, row=1)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
