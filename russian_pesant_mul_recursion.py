def mul(a,b,ans):
    if a==0:
        print(ans)
        return
    if a%2!=0:
        ans+=b
    mul(a//2,b*2,ans)
    
a,b=map(int,input().split())
mul(a,b,ans=0)
