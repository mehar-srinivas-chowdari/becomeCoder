def gcd(a,b):
    a,b=b%a,a
    if a==0:
        return b
    x=gcd(a,b)
    return x
a,b=map(int,input().split())
print(gcd(a,b))
