import random
import math
import statistics

nums = [random.randint(1, 100) for р in range(100)] # создаем 100 случайных целых чисел
avg = statistics.mean(nums) # среднее
med = statistics.median(nums) # медиана
std = statistics.stdev(nums) # стандартное отклонение
root = math.sqrt(sum(nums)) # Округленное значение квадратного корня из суммы всех чисел.

print(f"Среднее: {avg:.2f}, Медиана: {med:.2f}, "
f"Стандартное отклонение: {std:.2f}, Корень из суммы: {root:.2f}")
