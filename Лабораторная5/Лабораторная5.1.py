import random
import string
from pathlib import Path

def randomen(len=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=len))

def made(dir, n=10, ext='.txt'):
    p = Path(dir)
    p.mkdir(parents=True, exist_ok=True)
    files = []
    for _ in range(n):
        f = p / (randomen(8) + ext)
        f.touch()
        files.append(f.absolute())
    return files

for f in made("/home/user/random_files"):
    print(f)
