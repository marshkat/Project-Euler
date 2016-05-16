# palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPalindrome(a):
    stringnum = str(a)
    i = 0
    while i in range(0,len(stringnum)//2):
        if stringnum[i] == stringnum[-(i+1)]:
            i = i+1
        else: 
            return False
    return True

def productPali(a,b):
    palis = []
    for i in range(a,9999):
        for j in range(b,9999):
            product =i*j 
            if checkPalindrome(product) == True:
                palis.append(product)
    return findMax(palis) 

def findMax(a):
    max = 0
    for i in range(0,len(a)):
        if a[i]> max:
            max = a[i]
    return max
