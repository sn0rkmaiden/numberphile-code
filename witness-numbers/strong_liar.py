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
    x = 2^d * p + r \n    
    Checks if (a ** p) mod x == 1
    '''    
    assert x % 2 == 1
    assert a < x
    d = bin(x - 1)[2:][::-1].find('1')    
    p = (x - 1) // 2 ** d
    return sqam(a, p, x)['res'] == 1


x = 91
for a in range(1, x):
    if miller_rabin(x, a):
        print(a)