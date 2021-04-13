
#a
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


#Inverse number
#b
def euclidean_gcd(a, b):
    if a == 0:
        return 0, 1
    else:
        t, s = euclidean_gcd(b % a, a)
        print("s={0} a={1} t={2} b={3}".format(s,a,t,b))
        return  s - (b // a) * t, t


#c
def keys(L):
    # find the maximal number that comopsed by the given number of bits
    num = (2 ** L) - 1
    ##TODO:continue the function

key_length = input("Please insert key length:")



print("Insert numbers a,b such that 0<a<b")
a = int(input("a value:"))
b = int(input("b value:"))

print("Program will find the inverse number of {0} in Z{1} field by the Extended Euclidean algorithm process.".format(a,b))

print("Extended Euclidean algorithm process values:")
s,t = euclidean_gcd(b ,a)
print("The inverse number for the given a value is:" + str(t))



r,s,t = extended_eculidean_gcd(a,b)

print("gcd({0},{1}) = {0} * {2} + {1} * {3} = {4}".format(a,b,s,t,r))