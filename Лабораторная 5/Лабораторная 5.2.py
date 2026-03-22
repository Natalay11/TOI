import random
import math
import statistics

nums = [random.randint(1, 100) for _ in range(100)]
avg = statistics.mean(nums)
med = statistics.median(nums)
std = statistics.stdev(nums)
root = math.sqrt(sum(nums))

print(f"Среднее: {avg:.2f}, Медиана: {med:.2f}, "
f"Стандартное отклонение: {std:.2f}, Корень из суммы: {root:.2f}")
