# coding:utf8
# 入力された整数nを素因数分解する
def prime_factorization(n):
    ans = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n /= i
            ans.append(i)
        i += 1
    if n > 1:
        ans.append(n)
    return ans

# 入力された整数nを素因数分解して辞書で返す
# { key => 素因数, value => 素因数の個数 }
def prime_factorization_for_dict(n):
    ans = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n /= i
            ans[i] = 1 if i not in ans else ans[i] + 1
        i += 1
    if n > 1:
        ans[n] = 1 if n not in ans else ans[n] + 1
    return ans

# 入力された整数が素数かどうか判定する
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    else:
        return True
