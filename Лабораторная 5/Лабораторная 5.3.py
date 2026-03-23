import random
import json
import string

names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Laura"] # спикок имен
surnames = ["Doe", "Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia"] # спикок фамилий
name = random.choice(names) + " " + random.choice(surnames) # генерируется полное имя, случайное имя и фамилия
age = random.randint(18, 100) # генерируется случайный возраст до 100
email = name.lower().replace(" ", ".") + "@" + random.choice(["example.com", "test.com"]) # имя в нижний регистр, добавляется собака и рандомный почтовик
pwd_len = 12 # длинна пароля
chars = string.ascii_letters + string.digits + string.punctuation # берутся асци, буквы и знаки пунктуации и цифры, склыдываю в один список
password = ''.join(random.choice(chars) for _ in range(pwd_len)) # генерируется пароль по такому же принципу что и в 1 задании

data = {"name": name, "age": age, "email": email, "password": password} # полная информация

with open("user.json", "w") as f: # окрываю файл для записи
    json.dump(data, f, indent=4) # вписываю всю информацию о пользователе в джисон фай

with open("user.json") as f: # октываю джисон файл, заганяется в джисон дата с 4 пробелами
    print(json.dumps(json.load(f), indent=4)) # вывод загоняем в формат питон, превращаем в джисон строку
