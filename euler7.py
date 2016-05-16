


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

#10,001 st prime

def isprime(num):
    if num <2:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num > 2:
        for i in range(2,num//2+1):
            if num%i == 0:
                return False
    return True

def nthprime(a):
    count = 0
    working = 2
    while count < a:
        if isprime(working):
            count = count +1
            prime = working
            working = working + 1
        else:
            working = working + 1
    return prime 			