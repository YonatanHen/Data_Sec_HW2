# function
# extended_gcd(a, b)
# (old_r, r) := (a, b)
# (old_s, s) := (1, 0)
# (old_t, t) := (0, 1)
#
# while r ≠ 0 do
# quotient := old_r
# div
# r
# (old_r, r) := (r, old_r − quotient × r)
# (old_s, s) := (s, old_s − quotient × s)
# (old_t, t) := (t, old_t − quotient × t)
#
# output
# "Bézout coefficients:", (old_s, old_t)
# output
# "greatest common divisor:", old_r
# output
# "quotients by the gcd:", (t, s)


def extended_gcd(a,b):
    old_r, r = a,b
    old_s,s = 1,0
    old_t,t = 0,1

    while r != 0:

        q = old_r // r
        old_r,r = r, old_r - q * r
        old_s,s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    print("gcd({0},{1}) = {2} = {3} * {4} + {5} * {6}".format(a,b,old_r,a,old_s,b,old_t))
    print("greatest common divisor: {0}".format(old_r))
    if old_r == 1:
        print("{0},{1} are co-prime.".format(a,b))
    else:
        print("{0},{1} are not co-prime.".format(a, b))

extended_gcd(90,950)