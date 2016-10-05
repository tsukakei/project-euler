from euler_lib import prime_factorization
def ans():
    n = 600851475143
    table = prime_factorization(n)
    return str(table[-1])

if __name__ == '__main__':
    print ans()
