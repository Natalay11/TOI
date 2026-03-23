import random
import datetime
from array import array

today = datetime.date.today() # сегодня
start = today - datetime.timedelta(days=5*365) # пять лет назад

dates = []
for _ in range(10):
    days = random.randint(0, (today - start).days) # выбор 1 рандомную дату от 0 до целого числа дня из разности
    dates.append(start + datetime.timedelta(days=days)) # вносим в список начальную дату + превращеное дельтовое число количество дней которые прибовляются к дате

ords = array('l', (d.toordinal() for d in dates)) # добавляю в массив все даты из списка предварительно конвертируя из даты в порядковый номер

for i in range(len(ords)-1): # длинна массива минус 1, чтобы не сбивалась нумерация
    d1 = datetime.date.fromordinal(ords[i]) # первая дата, первый и следующий элемент массива конвертирую в дату
    d2 = datetime.date.fromordinal(ords[i+1]) # таакже для второй
    diff = abs((d2 - d1).days) # модуль их разницы целым числом
    print(f"Разница между {d1} и {d2}: {diff} дней") # вывожу разницу и промежуток 
