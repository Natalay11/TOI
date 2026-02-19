X = input("Введите число: ")
if X.isdigit():
    X = int(X)
    if X>=18:
        print ("Вы совершенолетний.")
    else:
        print ("Вы несовршенолетний")
else: print("Ошибка: Данные некорректны")
