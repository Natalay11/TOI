import math
# Задание 4.1.1
spisok = [i**2 for i in range(1,11)]
spisok.sort()
print(spisok)

# Задание 4.1.2
nomer = [1,2,3,4,5,6,7]
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
clovar = {nomer:day for (nomer,day) in zip(nomer,day) }
print(clovar)

# Задание 4.1.3
cpisok = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
ctroch = [cpisok.lower() for cpisok in cpisok]
print(ctroch)

# Задание 4.1.4
cardinal = [1, 3, 4, 87, 98, 15, 7, 4]
even = [i for i in cardinal if i%2==0]
print(even)

# Задание 4.1.5
kluzhi = [1, 2, 3, 4, 5]
fact = {kluzhi: math.factorial(kluzhi) for kluzhi in kluzhi}
print (fact)
