def largestpalindromeproduct():

    highest = '998001'
    

    
    l = 10000
    x1 = 100
    x2 = 1

    while int(h) > l:
        if h == h[::-1]:
            if int(h)%x1 == 0 and len(str(int(h)//x1)) == 3:
                x2 = int(h)//x1
                return h
            else:
                x1 += 1
        h = str(int(h) - 1)
            
