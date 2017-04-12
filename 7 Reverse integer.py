# Author: Steven Wang    Date: 20170411
# 7 reverse integer

a = 1563847412
b = -321
c = 100
d = 10001

def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    array = []   
    sign = 1 if x >= 0 else -1
    x = x*sign
    d = 1000000000
    sentinel = 0

    for i in range(10):
        
        quotient = x // d
        if quotient != 0:
            sentinel = 1

        if sentinel == 1:
            array.append(quotient if quotient != 0 else 0)
            x -= quotient*d

        d = d // 10

    result = 0
    m = 10 ** (len(array) -1)
    for i in range(len(array)):
        result += array[-i-1]*m
        m //= 10
    
    if result > 2**31:
        return 0

    result *= sign
    return result

    
    
    
    
    return 

print(reverse(a))
print(reverse(b))
print(reverse(c))
print(reverse(d))



        