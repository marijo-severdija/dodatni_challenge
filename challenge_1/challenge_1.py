import json

users_new = []

with open("users.json", "r") as file:
    users = json.loads(file.read())

"""for item in users:
    print(item)
    print(item["name"])
    print(item["name"].split())"""

for item in users:
    item["first_name"] = item["name"].split()[0]
    item["last_name"] = item["name"].split()[1]
    users_new.append(item)

with open("users_new.json", "w") as file:
    file.write(json.dumps(users_new, indent=4))

with open("users_new.json", "r") as file:
    users_print = json.loads(file.read())

for item in users_print:
    print(item["last_name"], item["first_name"], item["address"]["geo"]["lat"], item["company"]["catchPhrase"])
