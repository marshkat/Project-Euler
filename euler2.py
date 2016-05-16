#Euler project problem 2, sum of even fibonacci numbers less than 4,000,000


def evenFibSum(n):
    F=[1,2]
    fib = 3
    index = 2
    while fib < n:
        F.append(fib)
        fib = F[index] + F[index -1]
        index += 1
    even = []
    for i in range(0,len(F)):
        if F[i]%2 == 0:
            even.append(F[i])	
    sum = 0
    for i in range(0,len(even)):
        sum += even[i]	
    return sum

	

def fibarray(n):
    F=[1]
    fib = 2
    index = 1
    while fib < n:
        F.append(fib)
        fib = F[index] + F[index -1]
        index += 1
    return F

print(evenFibSum(4000000))