import random  # random is part of the given miller-rabin algorithm


def find_d_r(n):
    for r in range(n):
        for d in range(n):
            if (d * 2 ** r + 1 == n):
                return d, r


def prime(n, k):
    # find the maximal number that comopsed by the given number of bits
    num = (2 ** n) - 1
    if num % 2 == 0:
        return False

    alpha = 2
    d, r = find_d_r(num)

    for _ in range(k):
        # Pick a random number in [2..n-2]
        # make sure that n > 4
        a = 2 + random.randint(1, num - 4)

        x = (a ** d) % num
        if x == 1 or x == num - 1:
            continue
        for _ in range(r - 1):
            x = (x ** 2) % num
            if x == num - 1:
                break
        return num, alpha
    return False


print(prime(3,5))
