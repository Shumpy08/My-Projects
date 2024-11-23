from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

label = Label(text="is equal to", font=("Arial", 24, "italic"))
label.grid(column=0, row=2)

input = Entry(width=10)
input.grid(column=1, row=1)

label_2 = Label(text=0)
label_2.grid(column=1, row=2)


def calculate():
    number = int(input.get())
    new_number = round(number * 1.609, 2)
    label_2.config(text=new_number)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

miles = Label(text="Miles")
miles.grid(column=2, row=1)

km = Label(text="Km")
km.grid(column=2, row=2)


window.mainloop()
