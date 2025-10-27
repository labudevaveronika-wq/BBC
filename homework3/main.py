import random
from random import randint

n, m = int(input()), int(input())
pospx = 1
pospy = 1
posex = randint(2, n-2)
posey = randint(2, m-2)
keyx = [i for i in range(2, n) if i != posex]
keyy = [i for i in range(2, n) if i != posex]
key_flag = False
poskx = random.choice(keyx)
posky = random.choice(keyy)

massive_for_player = []
for i in range(n+1):
    row = []
    for j in range(m+1):
        if i == 0 or j == m or i == n or j == 0: row.append('.')
        else: row.append('#')
    massive_for_player.append(row)


hidden_massive = []
for i in range(n+1):
    row = []
    for j in range(m+1):
        if i == 0 or j == m or i == n or j == 0: row.append('.')
        else: row.append('#')
    hidden_massive.append(row)
for i in range(n + 1):
    for j in range(m + 1):
        if i == pospy and j == pospx: hidden_massive[i][j] = "P"
        elif i == posey and j == posex: hidden_massive[i][j] = "E"
        elif i == posky and j == poskx: hidden_massive[i][j] = "K"
    continue


while (pospx != posex or pospy != posey) or key_flag == False:
    massive_for_player[pospy][pospx] = hidden_massive[pospy][pospx]
    for i in range(n+1):
        for j in range(m+1):
            if i == pospy and j == pospx: print("P", end= " ")
            else: print(massive_for_player[i][j], end=" ")
        print()

    act = str(input())
    massive_for_player[pospy][pospx] = "#"
    new_px, new_py = pospx, pospy

    if act == 'w': new_py -= 1
    elif act == 's': new_py += 1
    elif act == 'd': new_px += 1
    elif act == 'a': new_px -= 1
    if new_px == poskx and new_py == posky: key_flag = True

    if 1 <= new_px <= m and 1 <= new_py <= n: pospx, pospy = new_px, new_py
    else: print("Нельзя совершить такое действие")
    massive_for_player[pospy][pospx] = "P"
print("Вы выиграли!")
# w - вверх
# a - влево
# s - вниз
# d - вправо
