from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

label = Label(text="I am a Label", font=("Arial", 24, "italic"))
label.config(text="new text")
label.grid(column=0, row=0)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label["text"] = new_text


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="Click me too")
button_2.grid(column=2, row=0)

input = Entry(width=12)
input.grid(column=3, row=2)

window.mainloop()
