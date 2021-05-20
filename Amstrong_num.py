num=int(input())
nn,n=num,num
count=0
while(num):
    count+=1
    num//=10
temp=0
while(n):
    temp=temp+pow(n%10,count)
    n//=10
if nn==temp:
    print('Amstrong')
else:
    print('Not Amstrong')
