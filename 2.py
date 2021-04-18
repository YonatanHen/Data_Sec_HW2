import random  # random is part of the given miller-rabin algorithm

#Utility function
def find_d_r(n):
    """function find d and r of the given algorithm"""
    for r in range(n):
        for d in range(n):
            if (d * 2 ** r + 1 == n):
                return d, r

#################### section a #######################################
def prime(n, k):
    """find the maximal number that composed by the given number of bits"""
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


#################### section b #######################################
def privetAndPublicCreate(p, alpha):
    """The idea is to chose randomly a number x between 1 to p-1, and a public number that will be alpha^x mod p"""
    priv_k = random.randint(1, p - 1)
    pub_k = (alpha ** priv_k) % p
    print(f'(*) privat key: {priv_k}')
    print(f'(*) public key: {pub_k}')

    #################### section c #######################################

    def mixedKeys(priv_k_b):
        """the idea is to get the value y (the private number of the other side, and to bundle it together with
        alpha^x, with the formula : alpha^(x*y) mod p"""
        return alpha ** (priv_k * priv_k_b) % p

    return mixedKeys


res = prime(4, 5)

if res:
    print(f'(*) P: {res[0]}.\n(*) Alpha: {res[1]}.')

    x = privetAndPublicCreate(res[0], res[1])
    print(f'(*) bundled number is: {x(5)}')

else:
    print('The entered number is not prime')
