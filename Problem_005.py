def Smallestmultiple():
    k = 2
    L = list(range(1, 21))
    while True:
        for j in L:
            if j == 20 and k%j == 0:
                return k
            elif k%j == 0:
                continue
            else:
                break
        k += 1
