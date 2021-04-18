from numpy import random

# utility functions
def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)


def lcm(x, y):
    return x * y // gcd(x, y)


def repetitive_Squaring(base, power, mod):
    if power == 0:
        return 1
    n = 1
    while power > 1:
        if power % 2 == 0:
            base = base * base
            base = base % mod
            power = power / 2
        else:
            n = base * n
            n = n % mod
            base = base * base
            base = base % mod
            power = (power - 1) / 2
    return (base * n) % mod


# Function return prime number in the given range
def findPrime(start, end):
    primes = []
    flag = True
    for i in range(start, end):
        for j in range(2, i // 2 + 1):
            if i % j == 0 and flag:
                flag = False
        if flag:
            primes.append(i)
        flag = True
    print(primes)
    return random.choice(primes)


#################### section a #######################################
def extended_eculidean_gcd(a, b):
    """Algorithm based on the instructions given in the lesson (taken from course book)"""
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t


#################### section b #######################################
def euclidean_gcd(num, mod):
    """Eculidean gcd algorithm function"""
    gcd, x, y = extended_eculidean_gcd(num, mod)

    if x < 0:
        x += mod

    return x


#################### section c #######################################
def keys(L):
    """Function find the private and the public keys according to the L bytes number which received as parameter"""
    # find p and q in range of 2**L to 2**(L+1) as showed in class (the must to be prime numbers)
    p = findPrime(2 ** L, 2 ** (L + 1))
    q = findPrime(2 ** L, 2 ** (L + 1))

    # calculate n
    n = p * q

    # find e as prime number in the range of 2**L to 2**(L+1)
    # e = findPrime(2 ** L, 2 ** (L + 1))
    e=65537
    print("Public key: (n, e) = ({0}, {1})".format(n, e))

    lambda_n = lcm(p - 1, q - 1)
    r, s, t = extended_eculidean_gcd(e, lambda_n)
    d=euclidean_gcd(e,lambda_n)

    print("Private key: (n, e, d) = ({0}, {1}, {2})".format(n, e, d))

    return (n, e), (n, e, d)

#################### section d #######################################
def RSA_encryption(publicKeyA, publicKeyB, privateKeyA, message):
    """Implementation of RSA as we learned in class"""
    print("Encryption:")
    n_a = publicKeyA[0]
    e = publicKeyA[1]
    d_a = privateKeyA[2]
    n_b = publicKeyB[0]
    encryptedMessage = repetitive_Squaring(message, e, n_b)
    print(f'n={n_a}')
    print(f'e={e}')
    print(f'd={d_a}')
    print()
    print(f'The encrypted message is: {encryptedMessage}')
    print("-------------------------------")
    return encryptedMessage


def RSA_decryption(publicKeyB, privateKeyB, message):
    """The function decrypts the encrypted message"""
    n_b = publicKeyB[0]
    e = publicKeyB[1]
    d_b = privateKeyB[2]
    decryptedMessage = repetitive_Squaring(message, d_b, n_b)
    print("Decryption:")
    print(f'n={n_b}')
    print(f'e={e}')
    print(f'd={d_b}')
    print()
    print(f'The decrypted message is: {decryptedMessage}')


message = 12345
publicKeyA, privateKeyA = keys(7)
publicKeyB, privateKeyB = keys(7)
m = RSA_encryption(publicKeyA,publicKeyB, privateKeyA, message)
RSA_decryption(publicKeyB, privateKeyB, m)

