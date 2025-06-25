#Mail


#Datetime module
import smtplib
import datetime as dt
import random


now = dt.datetime.now()
week = now.weekday()
if week == 2:

    with open("quotes.txt", "r") as quotes:
        babe = quotes.readlines()
        quote = random.choice(babe)
        print(quote)

    my_email = "codeniqqer08@gmail.com"
    password = "csyvqyyuaxzeosma"

    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="shumpy0808@gmail.com",
        msg=f"Subject:Fart\n\n{quote}"
    )
    connection.close()