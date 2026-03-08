def decorator(fufu):
    def wrapper(*args, **kwargs):
        print(f"Функция {fufu.__name__} вызвана с аргументами: ")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        resultat = fufu(*args, *kwargs)
        print(f"Площадь прямоугольника: {resultat}")
        return resultat
    return wrapper

@decorator
def square(l,h):
    return l * h
square(9,9)
