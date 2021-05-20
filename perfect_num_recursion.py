def perfect(n,temp,res):
    if temp:
        if n%temp==0:
            res+=temp
        ans=perfect(n,temp-1,res)
        return ans
    else:
        if(n==res):
            return("perfect num")
        else:
            return('not perfect num')

num=int(input())
print(perfect(num,num-1,0))
