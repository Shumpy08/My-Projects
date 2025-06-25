import smtplib
import datetime as dt
import random
import pandas

user_id = "codeniqqer08@gmail.com"
password = "csyvqyyuaxzeosma"

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])
        new_contents_2 = new_contents.replace("Hugh Ass", "Code Nigga")
        print(new_contents_2)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user_id, password=password)
        connection.sendmail(
            from_addr=user_id,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday\n\n{new_contents_2}"
        )
