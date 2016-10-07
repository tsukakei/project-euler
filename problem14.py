def collatz(n):
    length = 1;
    if n == 1:
        return length;
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def ans():
    max_len = 0;
    ans = 0
    for i in xrange(1, 1000001):
        i_len = collatz(i)
        if max_len < i_len:
            max_len = i_len
            ans = i
    return str(ans)

if __name__ == '__main__':
    print str(ans())
