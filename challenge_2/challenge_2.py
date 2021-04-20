import json
import datetime

with open("weather.json", "r") as file:
    weather = json.loads(file.read())

print(weather["name"])
print(weather["cod"])
print(weather["main"]["temp"])
print(weather["weather"][0]["description"], "\n")
print("sunrise: " + str(datetime.datetime.fromtimestamp(weather["sys"]["sunrise"])))
print("sunset: " + str(datetime.datetime.fromtimestamp(weather["sys"]["sunset"])))



