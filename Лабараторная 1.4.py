while True:
    X = input("Введите целое число: ")
    if X == "exit":
        break
    if X.lstrip('-').isdigit():
        print("Количество цифр:", len(X.lstrip('-')))
    else:
        print("Ошибка: введите целое число.")