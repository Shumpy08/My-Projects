from tkinter import *


window = Tk()
window.title("My Pass Manager")
window.config(padx=50, pady=50)

img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

web = Entry(width=35)
web.grid(row=1, column=1, columnspan=2)
web.focus()
usermail = Entry(width=35)
usermail.grid(row=2, column=1, columnspan=2)
usermail.insert(0, "Shumpy0808@gmail.com")
passw = Entry(width=21)
passw.grid(row=3, column=1)

generate = Button(text="Generate Password")
generate.grid(row=3, column=2)
add = Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
