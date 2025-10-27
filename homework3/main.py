posx = 1
posy = 1
n, m = int(input()), int(input())
for i in range(n+1):
    for j in range(m+1):
        if i == 1 and j == 1: print("P", end= " ")
        elif i == 0 or j == m  or i == n or j == 0: print('.', end=' ')
        else: print("*", end=" ")
    print()
