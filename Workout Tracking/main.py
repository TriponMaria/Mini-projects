from datetime import datetime
import os
import requests

exercise_input = input("Tell me which exercise you did: ")

GENDER = "female"
WEIGHT_KG = "59"
HEIGHT_CM = "169.0"
AGE = "24"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["sheet_endpoint"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()

DATE = datetime.now().date().strftime("%d/%m/%Y")
TIME = datetime.now().time().strftime("%X")
EXERCISE = exercise_data["exercises"][0]["user_input"]
DURATION = exercise_data["exercises"][0]["duration_min"]
CALORIES = exercise_data["exercises"][0]["nf_calories"]

headers = {
    "Authorization": "Basic bWFyaWFfdHJpcG9uOmFiY2RlZmdoaWo2NTQzMjEoKiop"
}

sheety_parameters = {
    "workout":
        {"date": DATE,
         "time": TIME,
         "exercise": EXERCISE.title(),
         "duration": DURATION,
         "calories": CALORIES
         }
}
sheety_response = requests.post(url=sheet_endpoint, json=sheety_parameters, headers=headers)

