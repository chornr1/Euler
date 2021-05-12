def fibi(n):

    sum = 2
    f1 = 1
    f2 = 2
    fn = 0
    L = [1, 2]

    while fn < n:
        fn = f1 + f2
        L.append(fn)
        f1 = f2
        f2 = fn
        if fn%2 == 0:
            sum += fn

    print(sum)
