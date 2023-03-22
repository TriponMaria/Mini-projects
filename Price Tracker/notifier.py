import os
import smtplib

MY_EMAIL = os.environ['MY_EMAIL']
PASSWORD = os.environ['PASSWORD']


class Notifier:
    def __init__(self):
        self.message = ""

    def send_email(self, product_name, price, webpage, email_to):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email_to,
                msg=f"Subject:Amazon price alert\n\n{product_name} is now {price}\n{webpage}".encode(encoding="utf-8", errors='ignore')
            )



