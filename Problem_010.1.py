n = 1000
L = [2]
for i in range(3, n):
    if i % 2 == 0:
        continue
    for j in range(3, i):
        if i % j == 0:
            break
    else:
        L.append(i)

print(sum(L))
