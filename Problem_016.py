def testPowerDigitSum(m):

    '''
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2**1000?
    '''

    k = 0 # Sum = 0
    n = 2
    s = str(n**m)
    
    for i in s:
        k += int(i)

    return k
