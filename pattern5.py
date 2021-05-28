num=int(input())
for i in range(1,num+1):
    if i%2==0:
        for j in range(1,num+1):
            print(i,end='')
    else:
        for j in range(num,0,-1):
            print(j,end='')
    print()
