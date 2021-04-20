import json

with open("users_new.json", "r") as file:
    user_find = json.loads(file.read())

query = input("Please enter last name for search: ")

for item in user_find:
    if query.lower() == item["last_name"].lower():
        print("name: " + item["name"], "\nemail: " + item["email"], "\ncompany: " + item["company"]["name"])
