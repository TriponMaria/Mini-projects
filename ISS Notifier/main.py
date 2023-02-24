from datetime import datetime
import requests
import smtplib
import time

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "your_password"
MY_LAT = 51.507351
MY_LONG = -0.127758


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if latitude in range(int(MY_LAT-5), int(MY_LAT+5)) and longitude in range(int(MY_LONG-5), int(MY_LONG+5)):
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    print(time_now)
    if time_now > sunset or time_now in range(0, sunrise):
        return True
    return False


while True:
    time.sleep(60)
    if is_dark() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="tripon.maria06@gmail.com",
                                msg="Subject:Lookup\n\nThe ISS is above you in the sky")

