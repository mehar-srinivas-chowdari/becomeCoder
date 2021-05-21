a,b=map(int,input().split())
r=1
while a:
    a,b=b%a,a
    if a==0:
        print(b)
