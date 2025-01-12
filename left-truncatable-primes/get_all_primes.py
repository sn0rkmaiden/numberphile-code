import random

def p(x):
    """ 
    Returns True if x is prime and False otherwise
    """
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

def is_probable_prime(n):
    """
    uses Miller-Rabin primality test 
    """
    if n==0 or n==1:
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1

    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(30):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite  


counter = 0

candidates = [str(x) for x in range(1, 10) if p(x)]
i = 0
while len(candidates) > 0:
    print(f'i={i} count={counter}')    
    counter += len(candidates)
    candidates = [str(a) + b for b in candidates for a in range(1, 10) if is_probable_prime(int(str(a) + b))]
    i += 1
    print(candidates)

print(counter)