def ans():
    ans = sum(i for i in xrange(1000) if (i % 3 == 0 or i % 5 == 0))
    return str(ans)

if __name__ == '__main__':
    print ans()
