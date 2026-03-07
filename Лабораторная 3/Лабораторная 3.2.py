print(
"Доступные операции:\n"
"1. Сложение\n"
"2. Вычитание\n"
"3. Умножение\n"
"4. Деление\n"
"5. Возведение в степень\n"
"6. Факториал\n"
"7. Среднее арифметическое\n"
"8. Квадратный корень\n"
"Для выхода введите Exit\n")
def one ():
    try:
        x = float(input("Введите первое слогаемое: "))
        y = float(input("Введите второе слогаемое: "))
        print(f"Сумма, {x+y}")
    except ValueError:
        print("Ошибка: введено не число")
def two():
    try:
        x = float(input("Введите уменьшаемое: "))
        y = float(input("Введите вычитаемое: "))
        print(f"Разность, {x - y}")
    except ValueError:
        print("Ошибка: введено не число")

def three():
    try:
        x = float(input("Введите первое умножаемое: "))
        y = float(input("Введите второе умножаемое: "))
        print(f"Произведение, {x * y}")
    except ValueError:
        print("Ошибка: введено не число")

def four():
    try:
        x = float(input("Введите делимое: "))
        y = float(input("Введите делитель: "))
        print(f"Частное, {x / y}")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except ValueError:
        print("Ошибка: введено не число")

def five():
    try:
        x = float(input("Введите основание: "))
        y = int(input("Введите показатель: "))
        print(f"Результат, {x**y}")
    except ValueError:
        print("Ошибка: введено не число")

def six():
    try:
        n = int(input("Введите число: "))
        if n < 0:
            raise ValueError("число не может быть отрицательным")
        x = 1
        for i in range(1, n + 1):
            x = x * i
        print(f"Факториал числа: {x}")
    except ValueError:
        print("Ошибка: введено не число")

def seven():
    try:
        a = (input("Введите числа через пробел: ").split())
        x = 0
        for i in a:
            i = float(i)
            x = x + i
        y: float = x / len(a)
        print(y)
    except ValueError:
        print("Ошибка: введено не число")

def eight():
    try:
        x = int(input("Введите число: "))
        if x < 0:
            raise ValueError("Число не может быть отрицательным")
        print(f"Результат, {x**0.5}")
    except ValueError:
        print("Ошибка: введено не число")
while True:
    try:
        Open = int(input("Введите операцию: "))
        if Open == "Exit":
            print("Выход из программы")
            break
        elif Open == 1:
            one()
        elif Open == 2:
            two()
        elif Open == 3:
            three()
        elif Open == 4:
            four()
        elif Open == 5:
            five()
        elif Open == 6:
            six()
        elif Open == 7:
            seven()
        elif Open == 8:
            eight()
    except ValueError:
        print("Ошибка: введено не число")
