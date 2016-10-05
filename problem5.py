from fractions import gcd

def ans():
    ans = 1
    for i in xrange(1, 21):
        ans *= i // gcd(i, ans)
    return str(ans)

if __name__ == '__main__':
    print ans()
