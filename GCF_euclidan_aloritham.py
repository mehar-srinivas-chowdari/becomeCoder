a,b=map(int,input().split())
while a:
    a,b=b%a,a
    if a==0:
        print(b)
