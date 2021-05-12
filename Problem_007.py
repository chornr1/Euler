def tenkprime(count):

    prime = 0
    #count = 10001
    i = 2
    while count > 0:
        
        flag = True
        for j in range(2, i):
            if i%j == 0:
               flag = False
               break
        if flag == True:
            prime = i
            count -= 1
        i += 1
        

    return prime, count
