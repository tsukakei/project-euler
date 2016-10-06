from euler_lib import prime_factorization_for_dict

def ans():
    triangle = 1
    count = 2
    while True:
        triangle += count
        div_dict = prime_factorization_for_dict(triangle)
        div_num = 1
        for x in div_dict.values():
            div_num *= (x + 1)
        if 500 < div_num:
            return str(triangle)
        count += 1

if __name__ == '__main__':
    print ans()
