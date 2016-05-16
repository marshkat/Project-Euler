#Project Euler problem 1

def multSum(a,b,c):
    if c%a == 0:
        x = c//a-1
    else:
        x = c//a
    if c%b == 0:
        y = c//b-1
    else:
        y = c//b
    sum = a*(x*(x+1)/2)+b*(y*(y+1)/2)
    product = a*b
    if c%product == 0:
        z = c//product-1
    else:
        z = c//product
    fix = product*(z*(z+1)/2)
    total = sum - fix
    return int(total)

print(multSum(3,5,1000))

