import datetime as dt
import pandas as pd
import random
import smtplib

my_email="guptaanuj0812"
password="gqqtssunqymavwrp"

# 2. Check if today matches a birthday in the birthdays.csv

today = (dt.datetime.now().month, dt.datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data=pd.read_csv("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/Birthday wishes/birthday wisher by email/birthday-wisher by email/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    file_path=f"C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/Birthday wishes/birthday wisher by email/birthday-wisher by email/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )
