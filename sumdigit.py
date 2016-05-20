#this is a sum of digits function



def sumd(n):
    import math
    digit=math.floor(math.log(n,10))+1
    sum = 0
    curr=n
    i=1
    while i <=digit:
        sum=sum+int(curr%(10**i)/(10**(i-1)))
        curr=curr-curr%(10**i)
        i=i+1
    return sum