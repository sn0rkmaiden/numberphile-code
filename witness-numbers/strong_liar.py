def sqam(x, exponent, modulus):
    cnt = 0    
    expBin = bin(exponent)[2:]    
    res = x    
    for i in expBin[1:]:        
        res = (res * res) % modulus
        cnt += 1
        if i == '1':
            res = (x * res) % modulus
            cnt += 1        
    # print(f'Number of calculations: {cnt}')            
    return {'res': res, 'cnt': cnt}

def miller_rabin(x, a):
    '''
    x - odd number to be tested for being prime \n
    a - witness number less than x \n
    x = 2^m * d + 1 \n    
    Checks if (a ** p) mod x == 1
    '''    
    assert x > 2
    assert x % 2 == 1
    assert a < x
    n = x
    m = 0
    x -= 1
    while (x % 2 == 0):
        m += 1
        x //= 2
    d = x        
    ans = sqam(a, d, n)['res'] 
    if ans + 1 == n:
        return True
    else:
        return ans == 1



s = {}
for x in range(3, 100, 2):    
    liars = []
    for a in range(1, x):
        if miller_rabin(x, a):
            liars.append(a)
    s[x] = liars
print(s)
