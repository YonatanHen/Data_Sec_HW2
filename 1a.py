def extended_eculidean_gcd(a,b):
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
    return(r,s,t)

a = 90
b = 950
r,s,t = extended_eculidean_gcd(a,b)

print("gcd({0},{1}) = {0} * {2} + {1} * {3} = {4}".format(a,b,s,t,r))