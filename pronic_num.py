def pronic(num):
    i=int(num**(1/2))
    if i*(i+1)==num:
        return(True)
    else:
        return(False)

num=int(input())
print(pronic(num))
