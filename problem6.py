def ans():
    sum_square = sum(i ** 2 for i in xrange(1, 101))
    square_sum = sum(i for i in xrange(1, 101)) ** 2
    ans = square_sum - sum_square
    return str(ans)

if __name__ == '__main__':
    print ans()
