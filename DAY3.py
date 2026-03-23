# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
fmovies= [input("movie1:"),input("movie2:"),input("movie3:")]
print(fmovies)
print(type(fmovies))

# WAP to check if a list contains a palindrome of elements.
plist=[1,2,3,2,1]
clist=plist.copy()
clist.reverse()

if(plist==clist):
    print("LIST IS PALLINDRONE")
else:
    print("no")

# WAP to count the number of students with the “A” grade in the following tuple.
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))
      
# Store the above values in a list & sort them from “A” to “D”
grade=("C","D","A","A","B","B","A")
grade=list(grade)
grade.sort()
print(grade)

# Write a program to create a list [10, 20, 30, 40].
# Replace 20 with 200, append 50, remove 30, and print the final list.
num=[10,20,30,40]
num[1]=200
num.append(50)
num.remove(30)
print(num)

# Write a program to create a list [5, 10, 15, 20].
# Insert 12 between 10 and 15,Print the final list

list=[5,10,15,20]
list.insert(2,12)
print(list)

# Write a program to create a tuple (1, 2, 3, 4, 5).
# Extract middle 3 elements using slicing,Print result

tup=(1,2,3,4,5)
tup=tup[1:4]
print(tup)
