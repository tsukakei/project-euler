from euler_lib import is_prime

def ans():
    cnt = 0
    ans = 1
    while cnt < 10001:
        ans += 1
        if is_prime(ans):
            cnt += 1
    else:
        return str(ans)

if __name__ == '__main__':
    print ans()
