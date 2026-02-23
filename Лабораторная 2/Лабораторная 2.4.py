W = input("Введите строку: ").lower().split()
WC = {}
for word in W:
    WC[word] = WC.get(word, 0) + 1
seen = set()
result = []
for word in W:
    if word not in seen:
        result.append(f"{word}: {WC[word]}")
        seen.add(word)
print("\n".join(result))