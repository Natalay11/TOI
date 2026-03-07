lists = input("Введите список чисел через пробел: ").split()
Mnozhetel = input("Введите множетель(по умолчанию 2): ")
z = []
if Mnozhetel == '':
    Mnozhetel = 2
else: Mnozhetel = int(Mnozhetel)
for i in lists:
    i = int(i)
    z.append(i)
def ymnozh (ls, mnozhetel: int) -> list:
    g = []
    for f in ls:
            f = f * mnozhetel
            g.append(f)
    return g
X = ymnozh(z , Mnozhetel)
Y = int
result = map(lambda x: x * Mnozhetel, z)
print(f"Результат (функция): {X}")
print(f"Результат (лямбда-функция): {list(result)}")