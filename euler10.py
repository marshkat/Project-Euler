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
