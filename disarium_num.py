def disarium(num):
    i,n=0,num
    while(num):
        num//=10
        i+=1
    temp=0
    while(n):
        r=n%10
        n//=10
        temp+=pow(r,i)
        i-=1
    return(temp)

num=int(input())
print(disarium(num)==num)
