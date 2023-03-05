import random

all_nums = []

x = 1
while x  <= 60:
    all_nums.append(x)
    x += 1



sena = []

x = 1
while x <= 6:
    sorteado = random.choice(all_nums)
    sena.append(sorteado)
    all_nums.remove(sorteado)
    x += 1

sena.sort()

print(all_nums)
print(sena)