def ans():
    ans = 0
    for i in xrange(100, 1000):
        for j in xrange(100, i):
            k = i * j
            s = str(k)
            if s == s[::-1] and ans < k:
                ans = k
    return str(ans)

if __name__ == '__main__':
    print ans()
