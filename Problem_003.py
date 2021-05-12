def primefactors(n):
    i = 1
    L = []
    while i < n:
        for j in range(i, n+1):
            if n%j == 0:
                break
        n = n//j
        i = j+1
        L.append(j)

    return j
            
