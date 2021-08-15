import requests
import datetime as dt
import os


SHEETY_ENDPOINT = "https://api.sheety.co/71bc7b155fe051bcc963ca24178a55d0/workoutTracking/workouts"
SHEETY_TOKEN = os.environ["SHEETY_API_KEY"]


sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


EXERCISE_APP_ID = "ddab7404"
EXERCISE_APP_KEY = os.environ["EXERCISE_APP_KEY"]
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_APP_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": input("What exercise would you like to log? "),
    "gender": "male",
    "weight_kg": 61.5,
    "height_cm": 170.18,
    "age": 24
}

with requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_headers) as response:
    response.raise_for_status()
    exercise_data = response.json()["exercises"]
    print(exercise_data)
for exercise in exercise_data:
    ex_name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    date = dt.datetime.now().strftime("%m-%d-%Y")
    time = dt.datetime.now().strftime("%H:%M")
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": ex_name.title(),
            "duration": duration,
            "calories": calories
        }
    }
    with requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers) as response:
        print(response.status_code)
        print(response.json())
