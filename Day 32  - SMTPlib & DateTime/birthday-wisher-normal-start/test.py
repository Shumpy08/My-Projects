import smtplib
import random
import pandas
import datetime as dt

user_id = "#####3"
password = "#####3"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthday_dict[today_tuple]

    with open(file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user_id, password=password)
        connection.sendmail(
            from_addr=user_id,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday Nigga\n\n{letter}"
        )