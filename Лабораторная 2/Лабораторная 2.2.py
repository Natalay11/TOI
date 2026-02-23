dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
keys = set(dct.keys())
values = set(dct.values())
combined = keys | values
print(f"Множество ключей: {keys}")
print(f"Множество значений: {values}")
print(f"Объединение множеств: {combined}")