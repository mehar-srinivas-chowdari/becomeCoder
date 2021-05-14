n= int(input())
num,c=0,-1
while n:
    r=n%10
    n=n//10
    c+=1
    num=num*10+r
f=num//pow(10,c)
l=num%10
num=num%pow(10,c)
num=num//10
num=num*10+f
num=l*pow(10,c)+num
print(num)
