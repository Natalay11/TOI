def muka(g:int):
    for i in range(2,g):
        if g%i==0:
            return False
    return True
X = int(input("Введите число: "))
Y = list(range(X+1))
Spisok = [i for i in Y if muka(i) == True]
print(Spisok)
