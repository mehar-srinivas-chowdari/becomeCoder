def count(num,dc):
    if num:
        num//=10
        return(count(num,dc+1))
    return dc
def disarium(num,dc,add):
    if num:
        r=num%10
        num//=10
        return(disarium(num,dc-1,add+pow(r,dc)))
    return add

num=int(input())
print(disarium(num,count(num,0),0)==num)
