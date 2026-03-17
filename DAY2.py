#QUE:- WAP TO FIND LENGHT OF FIRST NAME AFTER TAKING INPUT

name=str(input("ENTER UR FIRST NAME:-"))
lenght = len(name)
print(lenght)

#QUE :- WAP TO FIND OCCURNENCE OF $ IN STR

str="TODAY 1$ = 85 RUPEES AND 100 $ = 8500 RUPEE ALSO $ IS INCREASE DAY BY DAY "
print(str.count("$"))

#QUE-WAP to find occurrence of 'o' in a string.
str="Astrology is a awesome concept"
print(str.count("o"))

# WAP to check if a string starts with "Py" or not.
str1='Python'
str2='Awesome'
print(str1.startswith("Py"))
print(str2.startswith("Py"))

#WAP to replace all spaces in a string with _.
str="I LOVE CODE IN PYTHON"
print(str.replace(" ","_"))

 #WAP to count number of vowels in a string.
str="programming_victory"
count= str.count('a')+str.count('o')+str.count('e')+str.count('i')+str.count('u')
print(count)

# WAP to convert a string into uppercase.
str1="python"
str2="PYTHON"
print(str1.upper())
print(str2.lower())

# WAP to check if a number is even or odd.

num = int(input("ENTER NUMBER:-"))
if(num%2==0):
    print("NUMBER IS EVEN")
else:
    print("NUMBER IS ODD")

# WAP to check if a number is positive, negative, or zero.

num = int(input("ENTER NUMBER:-"))
if(num>0):
    print("POSITIVE")
elif(num<0):
    print("NEGATIVE")
else:
    print("zero")

# WAP to find the largest of two numbers.

num1 = int(input("ENTER NUMBER1:-"))
num2= int(input("ENTER NUMBER2:-"))
if(num1>num2):
    print("num1 is greater")
elif(num1<num2):
    print("num2 is greater")
else:
    print("BOTH ARE EQUAL")

# WAP to check if a number is divisible by 5.

num = int(input("ENTER NUMBER:-"))
if(num%5==0):
    print("NUMBER IS DIVISIBLE BY 5")
else:
    print("NUMBER IS NOT DIVISIBLE BY 5")

# WAP to check if a password is "admin123" or not.

password=input("ENTER PASSWORD:")
if(password=="admin123"):
    print("ACESS APPROVED")
else:
    print("ACESSS DENIED")