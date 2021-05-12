def LargestPalindromeProduct():

    c = 0
    L = []

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            c = i * j

            if (str(c) == str(c)[::-1]):
                L.append(c)
            else:
                continue

    return max(L)
