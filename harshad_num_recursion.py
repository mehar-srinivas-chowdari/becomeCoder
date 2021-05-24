def harshad(num,add):
    if num:
        r=num%10
        num//=10
        return(harshad(num,add+r))
    return add

num=int(input())
print(num%harshad(num,0)==0)
