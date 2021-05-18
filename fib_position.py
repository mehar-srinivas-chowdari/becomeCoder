def fib(num,pos=0,a=0,b=1,c=0):
    while(c<num):
        c=a+b
        a=b
        b=c
        pos+=1
        #print(c)
    if num==0:
        print(1)
        return
    if num==1:
        print(2)
        return
    if num==c:
        print(pos+2)
    else:
        print(False)
num=int(input())
fib(num)
    
