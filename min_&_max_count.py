num= int(input())
sa,la,lac,sac=9,0,0,0
while num:
    r=num%10
    num=num//10
    if r > la:
        la=r
        lac=1
    elif r==la:
        lac+=1
    if r < sa:
        sa=r
        sac=1
    elif r==sa:
        sac+=1
print(sa,la)
print(sac,lac)
