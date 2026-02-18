X = input("Введите число: ")
if X.isdigit():
    X = int(X)
    if X % 2 == 0: print("Число X является чётным")
    else: print("Число X не является чётным")
else: print("Ошибка: введено не число")