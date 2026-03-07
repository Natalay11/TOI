from typing import List

class ZootopiaCitizen:
    city_name: str = "Зверополис"
    districts: List[str] = ["Центр", "Тундра", "Пустыня", "Луга"]

    def __init__(self, species: str, name: str, age: int, profession: str, district: str) -> None:
        self.species: str = species
        self.name: str = name
        self.age: int = age
        self.profession: str = profession
        self.district: str = district
        self.friends: List[str] = []

    def __str__(self) -> str:
        return f"{self.name} ({self.species}), {self.age} лет, живёт в {self.district}, работает {self.profession}."

    def introduce(self) -> str:
        return f"Привет, я {self.name}, я {self.species}."

    def move(self, new_district: str) -> None:
        self.district = new_district

    def add_friend(self, friend_name: str) -> None:
        self.friends.append(friend_name)

    def work(self) -> str:
        return f"{self.name} работает {self.profession} в {self.district}."

judy = ZootopiaCitizen("Крольчиха", "Джуди", 26, "полицейский", "Центр")
nick = ZootopiaCitizen("Лис", "Ник", 32, "полицейский", "Луга")
bogo = ZootopiaCitizen("Буйвол", "Бого", 50, "начальник", "Центр")

print(judy)
print(nick.introduce())
judy.add_friend("Ник")
nick.move("Тундра")
print(nick.work())