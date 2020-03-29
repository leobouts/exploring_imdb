import random

# This function creates random values for the variable a, b of our hash function
def create_random_hash_functions(n, p=2**33-355):
    a = []
    b = []
    for i in range(n):
        tmp_a = random.randint(1, p-1)
        while (tmp_a in a):
            tmp_a = random.randint(1, p-1)
        
        tmp_b = random.randint(1, p-1)
        while (tmp_b in b):
            tmp_b = random.randint(0, p-1)
        
        a.append(tmp_a)
        b.append(tmp_b)
    return a, b


def hash_function(x, a, b, m, p=2**33-355):
    return (((a * x + b) % p) % m)
