#calculate the smallest number that is evenly divisible by all integers less than 20

#Need to factor each number and return factors with multiplicity
def findprimes(b):
    A=[]
    for i in range(0,b+1):
        A.append(i)
    for j in range(2,(b//2)+1):
        n=2
        if A[j]==0:
            pass
        else:
            while n <= b/j:
                A[j*n]=0
                n=n+1
    k=0
    L=len(A)
    while k<L:
        if A[k]==0:
            del A[k]
            L=len(A)
        else:
            k=k+1
    return A[1:]
	
def smallestMultiple(b):
    A = findprimes(b)
    product = 1
    for j in A:
        i = 0
        while j**i <= b:
            i = i+1
        max = i-1
        product = product*j**max
    return product

def countMult(A,a):
    mult = 0
    for i in range(0,len(A)):
        if A[i] == a:
            mult = mult + 1
    return mult

def factor(prime,a):
    i = 2
    while i <= a:
        if i == a:
            prime.append(a)
            break
        if a/i == a//i:
            factor1 = i
            factor2 = a//i
            factor(prime,factor1)
            factor(prime,factor2)
            break
        else:
            i = i+1
    return prime



