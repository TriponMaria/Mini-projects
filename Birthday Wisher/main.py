import datetime as dt
import os
import pandas
import random
import smtplib

my_email = os.environ['my_email']
password = os.environ['password']

now = dt.datetime.now()
current_day = now.day
current_month = now.month
today = f"{current_month}-{current_day}"
birthday_data = pandas.read_csv("birthdays.csv")
birthday_info = birthday_data.to_dict(orient="records")
random_letter_number = random.randint(1, 3)

for birthday_person in birthday_info:
    with open(f"letter_templates/letter_{random_letter_number}.txt", 'rt') as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", f"{birthday_person['name']}")
    if today == f"{birthday_person['month']}-{birthday_person['day']}":
        print(f"Today is {birthday_person['name']}'s birthday.")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy birthday!\n\n{letter}")