from numpy import random

# utility functions
def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)


def lcm(x, y):
    return x * y // gcd(x, y)


# def repetitive_Squaring(num, exp, mod):
#     if exp < 0:
#         return repetitive_Squaring((1 / num) % mod, -exp, mod)
#     elif exp == 0:
#         return 1 % mod
#     elif exp == 1:
#         return num % mod
#     elif exp % 2 == 0:
#         return repetitive_Squaring((num * num) % mod, (exp / 2), mod) % mod
#     else:
#         return (num * repetitive_Squaring((num * num) % mod, (exp - 1) / 2, mod)) % mod

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
        for j in range(2, i//2+1):
            if i % j == 0 and flag:
                flag = False
        if flag:
            primes.append(i)
        flag = True
    print(primes)
    return random.choice(primes)



#################### section a #######################################
# Algotihm based on the instructions given in the lesson (taken from course book)
def extended_eculidean_gcd(a, b):
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
# Find inverse number
# def euclidean_gcd(a, b):
#     if a == 0:
#         return 0, 1
#     else:
#         t, s = euclidean_gcd(b % a, a)
#         print("s={0} a={1} t={2} b={3}".format(s, a, t, b))
#         return s - (b // a) * t, t
def euclidean_gcd(num, mod):

    gcd, x, y = extended_eculidean_gcd(num, mod)

    if x < 0:
        x += mod

    return x


#################### section c #######################################
def keys(L):
    # find p and q in range of 2**L to 2**(L+1) as showed in class (the must to be prime numbers)
    p = findPrime(2 ** L, 2 ** (L + 1))
    q = findPrime(2 ** L, 2 ** (L + 1))

    # calculate n
    n = p * q

    # find e as prime number in the range of 2**L to 2**(L+1)
    e = findPrime(2 ** L, 2 ** (L + 1))

    print("Public key: (n, e) = ({0}, {1})".format(n, e))

    lambda_n = lcm(p - 1, q - 1)
    r, d, t = extended_eculidean_gcd(e, lambda_n)

    print("Private key: (n, e, d) = ({0}, {1}, {2})".format(n, e, d))

    return (n, e), (n, e, d)


L = int(input("Please insert key length:"))

private_key, public_key = keys(L)

#################### section d #######################################
# Implementation of RSA as we learned in class
def RSA_encryption(p_a, q_a, p_b, q_b, e, message):
    print("Encryption:")
    n_a = p_a * q_a
    n_b = p_b * q_b
    phi = (p_a - 1) * (q_a - 1)
    lam = lcm(p_a - 1, q_a - 1)
    d_a = euclidean_gcd(e, lam)
    encryptedMessage = repetitive_Squaring(message, e, n_b)
    print(f'n={n_a}')
    print(f'φ(n)={phi}')
    print(f'λ(n)={lam}')
    print(f'e={e}')
    print(f'd={d_a}')
    print()
    print(f'The encrypted message is: {encryptedMessage}')
    print("-------------------------------")
    return d_a, n_a, encryptedMessage

def RSA_decryption(p_b, q_b, e, message):
    n_b = p_b * q_b
    phi = (p_b - 1) * (q_b - 1)
    lam = lcm(p_b - 1, q_b - 1)
    d_b = euclidean_gcd(e, lam)
    decryptedMessage = repetitive_Squaring(message, d_b, n_b)
    print("Decryption:")
    print(f'n={n_b}')
    print(f'φ(n)={phi}')
    print(f'λ(n)={lam}')
    print(f'e={e}')
    print(f'd={d_b}')
    print()
    print(f'The decrypted message is: {decryptedMessage}')

p_a = 2000303
q_a = 2000387
p_b = 2000423
q_b = 2000807
e = 65537
message = 1234567
d_a, n_a, m = RSA_encryption(p_a, q_a, p_b, q_b, e, message)
RSA_decryption(p_b, q_b, e, m)

#
# print("Insert numbers a,b such that 0<a<b")
# a = int(input("a value:"))
# b = int(input("b value:"))
#
# print("Program will find the inverse number of {0} in Z{1} field by the Extended Euclidean algorithm process.".format(a,b))
#
# print("Extended Euclidean algorithm process values:")
# s,t = euclidean_gcd(b ,a)
# print("The inverse number for the given a value is:" + str(t))


#
# r,s,t = extended_eculidean_gcd(a,b)
#
# print("gcd({0},{1}) = {0} * {2} + {1} * {3} = {4}".format(a,b,s,t,r))
