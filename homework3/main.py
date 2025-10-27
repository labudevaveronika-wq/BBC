import random
from random import randint

n, m = int(input()), int(input())
n += 2
m += 2
pospx = 1
pospy = 1
key_flag = False
sword_flag = False
posex = randint(2, n-2)
posey = randint(2, m-2)
keyx = [i for i in range(2, n-2) if i != posex]
keyy = [i for i in range(2, n-2) if i != posex]
poskx = random.choice(keyx)
posky = random.choice(keyy)
swordx = [i for i in range(2, n-1) if i != posex and i != poskx]
swordy = [i for i in range(2, n-1) if i != posex and i != posky]
possx = random.choice(swordx)
possy = random.choice(swordy)
monsterx = [i for i in range(2, n-1) if i != posex and i != poskx and i != possx]
monstery = [i for i in range(2, n-1) if i != posex and i != posky and i != possy]
posmx = random.choice(swordx)
posmy = random.choice(swordy)


massive_for_player = []
for i in range(n+2):
    row = []
    for j in range(m+2):
        if i == 0 or j == m-1 or i == n-1 or j == 0: row.append('.')
        else: row.append('#')
    massive_for_player.append(row)


hidden_massive = []
for i in range(n+2):
    row = []
    for j in range(m+2):
        if i == 0 or j == m-1 or i == n-1 or j == 0: row.append('.')
        else: row.append('#')
    hidden_massive.append(row)
for i in range(n):
    for j in range(m):
        if i == pospy and j == pospx: hidden_massive[i][j] = "P"
        elif i == possy and j == possx: hidden_massive[i][j] = "S"
        elif i == posmy and j == posmx: hidden_massive[i][j] = "M"
        elif i == posey and j == posex: hidden_massive[i][j] = "E"
        elif i == posky and j == poskx: hidden_massive[i][j] = "K"
    continue


while (pospx != posex or pospy != posey) or key_flag == False:
    massive_for_player[pospy][pospx] = hidden_massive[pospy][pospx]
    for i in range(n):
        for j in range(m):
            if i == pospy and j == pospx: print("P", end= " ")
            else: print(massive_for_player[i][j], end=" ")
        print()

    act = str(input())
    if not (pospx == poskx and pospy == posky or pospx == posex and pospy == posey or pospx == possx and pospy == possy and pospx == posmx and pospy == posmy):
        massive_for_player[pospy][pospx] = "#"
    new_px, new_py = pospx, pospy

    if act == 'w': new_py -= 1
    elif act == 's': new_py += 1
    elif act == 'd': new_px += 1
    elif act == 'a': new_px -= 1
    if new_px == possx and new_py == possy:
        print("Вы нашли меч!")
        input("Нажми Enter чтобы продолжить...")
        massive_for_player[possy][possx] = "S"
    if new_px == posmx and new_py == posmy:
        if sword_flag == True:
            print("У Вас есть меч, Вы победили монстра!")
            input("Нажми Enter чтобы продолжить...")
            massive_for_player[posey][posex] = "M"
        else:
            print("К сожалению, у Вас нет меча, монстр напал на Вас!")
            input("Нажми Enter чтобы продолжить...")
            massive_for_player[posey][posex] = "M"
    if new_px == posex and new_py == posey:
        if key_flag == True:
            print("Вы выиграли!")
            break
        else:
            print("Вы нашли портал, но у вас нет ключа, найдите его и возвращайтесь!")
            input("Нажми Enter чтобы продолжить...")
            massive_for_player[posey][posex] = "E"
    if new_px == poskx and new_py == posky:
#        print("!!!")
        key_flag = True
        print("Ты нашел(ла) ключ, надо дойти до портала!")
        input("Нажми Enter чтобы продолжить...")
        massive_for_player[posky][poskx] = "K"

    if 1 <= new_px < m-1 and 1 <= new_py < n-1: pospx, pospy = new_px, new_py
    else: print("Нельзя совершить такое действие")

# w - вверх
# a - влево
# s - вниз
# d - вправо
