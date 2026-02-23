X = list(map(int, input("Введите первый список: ").split()))
Y = list(map(int, input("Введите второй список: ").split()))
C = set(X).intersection(Y)
S = set()
result = []
for num in X:
    if num in C and num not in S:
        result.append(str(num))
        S.add(num)
print("Общие элементы:", ' '.join(result))