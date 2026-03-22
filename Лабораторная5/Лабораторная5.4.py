import random
import datetime
from array import array

today = datetime.date.today()
start = today - datetime.timedelta(days=5*365)

dates = []
for _ in range(10):
    days = random.randint(0, (today - start).days)
    dates.append(start + datetime.timedelta(days=days))

ords = array('l', (d.toordinal() for d in dates))

for i in range(len(ords)-1):
    d1 = datetime.date.fromordinal(ords[i])
    d2 = datetime.date.fromordinal(ords[i+1])
    diff = abs((d2 - d1).days)
    print(f"Разница между {d1} и {d2}: {diff} дней")
