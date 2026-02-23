X = input("Введите числа через пробел:")
Y = int(input("Введите степень: "))
W = X.split()
Z1 = []
Z2 =[]
for f in W:
    if not f.isalpha(): f= float(f)
    Z1.append(f)
for f in Z1:
    if isinstance(f, float):
        f2 = f**Y
        Z2.append(f2)
    else :
        Z2.append(f*Y)
print(Z2)