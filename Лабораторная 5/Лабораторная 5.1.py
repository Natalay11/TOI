import random
import string
from pathlib import Path

def randomen(len=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=len)) # возвращаем обединение количества строк,
# choices выберает рандомную букву из асци и цифру, возвращает список с указаной длинной, в итоге превращаю в одну строку

def made(dir, n=10, ext='.txt'):
    p = Path(dir) #превращает строку в путь
    p.mkdir(parents=True, exist_ok=True) #создаю папку, parents автоматически создает недостающие папки
    files = []
    for i in range(n): #
        f = p / (randomen(8) + ext) # полный путь для файла
        f.touch() # создаю файл
        files.append(f.absolute()) # добовляется путь файла в лист
    return files

for f in made("/home/user/random_files"): # вызываем функцию для каждого ф
    print(f)
