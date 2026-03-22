import random
import json
import string

names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Laura"]
surnames = ["Doe", "Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia"]
name = random.choice(names) + " " + random.choice(surnames)
age = random.randint(18, 100)
email = name.lower().replace(" ", ".") + "@" + random.choice(["example.com", "test.com"])
pwd_len = 12
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(pwd_len))

data = {"name": name, "age": age, "email": email, "password": password}

with open("user.json", "w") as f:
    json.dump(data, f, indent=4)

with open("user.json") as f:
    print(json.dumps(json.load(f), indent=4))
