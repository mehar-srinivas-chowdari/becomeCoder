num=int(input())
res=0
for i in range(1,num):
    if num%i==0:
        res+=i
if  res==num:
    print('PERFECT NUMBER')
else:
    print('NOT PERFECT NUMBER')
