##WHILE_LOOPS
#Q1:WAP TO PRINT HELLO PYTHON 1000 TIMES.
i=1
while i<=1000:
    print("HELLO PYTHON",i)
    i+=1

#Q2:Print numbers from 1 to 100.
num=1
while num<=100:
    print(num)
    num+=1 

# Q3:Print numbers from 100 to 1.
num=100
while num>=1:
    print(num)
    num-=1

# Q4:Print the multiplication table of a number n.
num=int(input("ENTER NUMBER OF TABLE:-"))
i=1
while i<=10:
    table=num*i
    i+=1
    print(table)

# Q5:Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1

## BREAK && CONTINUE 
# Q6:QSearch for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100,88,65]

tup=(1, 4, 9, 16, 25, 36, 49, 64, 81,100,88,65)
x=int(input("ENTER ELEMENT WANT TO FIND:"))
idx=0
while idx<len(tup):
    if(x==tup[idx]):
        print("Element found at index :",idx)
        break
    else:
        print("Finding.....")
    idx+=1

#Q7: Print ODD NUMBERS BETWEEN 1 TO 100
i=1
while i<=100:
    if(i%2==0): #FOR EVEN CONDITION IS (i%2!=0)
        i+=1
        continue #skip
    print(i)
    i+=1

## FOR LOOP 
# Q8:Print the elements of the following list using a For loop:
# [1, 8, 9, 56, 25, 76, 54, 64, 30,10]

list=[1, 8, 9, 56, 25, 76, 54, 64, 30,10]
for elements in list:
    print(elements)
    
# Q9:Search for a number x in this tuple using loop:
# [1, 8, 9, 56, 25, 76, 54, 64, 30,10]

tup=(1, 8, 9, 56, 25, 76, 54, 64, 30,10)
x=int(input("ENTER X:"))
idx=0
for el in tup:
    if(x==el):
        print("Element found at idx:",idx)
        
        break
    idx+=1
# RANGE
# Print numbers from 1 to 100
for i in range(1,101):
    print(i)

# Print numbers from 100 to 1.
for i in range(100,0,-1):
 print(i)

# Print the multiplication table of a number n.
n=int(input("Enter n:"))
for i in range(1,11):
    print(n*i)

# WAP to find the sum of first n numbers. (using while)
n = int(input("Enter n: "))
sum = 0
i = 0

while i <= n:
    sum += i
    i += 1

print("Total addition:", sum)

# WAP to find the factorial of first n numbers. (using for)
n = int(input("Enter n: "))
fact=1

for i in range(n,1,-1):
    fact = fact*i

print("FACTORIAL:",fact)