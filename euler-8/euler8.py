#this is a program to take a list of numbers and find the maximum product of 13 consecutive numbers
#the list of numbers is stored in file euler8list.txt




filename=input()

#this concatenates the string of numbers by removing the newline
num=""
with open(filename, 'r') as f:
    for line in f:
        num=num+line.rstrip()



products=[]
#this cycles through 13 at a time and finds the product

stop=len(num)-13
for i in range(0,stop):
    j=0
    prod=1
    while j <= 12:
        prod=prod*int(num[i+j])
        j=j+1
    if prod==0:
        continue
    else:
        products.append(prod)
        
max=max(products)
print(max)

        	


