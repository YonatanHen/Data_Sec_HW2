#Inverse number

def euclidean_gcd(a, b):
    if a == 0:
        return 0, 1
    else:
        t, s = euclidean_gcd(b % a, a)
        print("s={0} a={1} t={2} b={3}".format(s,a,t,b))
        return  s - (b // a) * t, t

print("Insert numbers a,b such that 0<a<b")
a = int(input("a value:"))
b = int(input("b value:"))

print("Program will find the inverse number of {0} in Z{1} field by the Extended Euclidean algorithm process.".format(a,b))

print("Extended Euclidean algorithm process values:")
s,t = euclidean_gcd(b ,a)
print("The inverse number for the given a value is:" + str(t))
