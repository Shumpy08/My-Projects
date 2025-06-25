import random
from tkinter import *

import pandas
from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
try:
    new_data = pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    data = pandas.read_csv("data/JapaneseRomaji_to_English.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = new_data.to_dict(orient="records")
current_card = {}


def next_card():
    """Flips the card to next word"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Japanese (Romaji)", fill="black")
    canvas.itemconfig(card_word, text=current_card["JAPANESE"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the card to the translated word"""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["ENGLISH"], fill="white")
    canvas.itemconfig(card_image, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data: DataFrame = pandas.DataFrame(to_learn)
    print(len(data))
    data.to_csv("data/words_to_learn", index=FALSE)
    next_card()


# UI-SETUP
window = Tk()
window.title("FartCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_mark = PhotoImage(file="images/wrong.png")
tick_mark = PhotoImage(file="images/right.png")

wrong_button = Button(image=cross_mark, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=tick_mark, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
