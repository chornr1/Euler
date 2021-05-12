'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a*a + b*b = c*c
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

'''
a + b + c = 1000
c = 1000 - (a + b)
2000*(a + b) = 1000*1000 + 2*a*b
2000 * (a + b) - 2*a*b = 1000000
'''

a, b, c = 0, 0, 0
for i in range(1, 1000):
    for j in range(1, 1000):
        a = i
        b = j
        c = (1000 - (a + b))
        if (2000 * (a + b) - 2*a*b == 1000000):
            if (a + b + c == 1000):
                print(a *b *c)
                break
        
                
