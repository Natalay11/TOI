def text(texts: str, filename: str):
    file = open(filename, "a", encoding="utf-8")
    file.write(f"\n{texts}")
    file.close()
    y = open("text 1.txt","r", encoding="utf-8")
    s = y.readlines()
    for index, line in enumerate(s, start=1):
        if index % 2 == 0:
            print(f"{line}")
    y.close()
biba = "Хочу спать:)"
boba = "text 1.txt"
text(biba, boba)