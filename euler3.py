prime = []

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

def Left(i):
    return 2*i+1

def Right(i):
    return 2*i+2

def heapify(A,i):
    l = Left(i)
    r = Right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l 
    else:
        largest = i 
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        key = A[largest]
        A[largest] = A[i]
        A[i] = key
        heapify(A,largest)

def buildheap(A):
    for i in range(len(A)//2,-1,-1):
        heapify(A,i)
    return A

buildheap(factor(prime,600851475143))
print(prime[0]) 