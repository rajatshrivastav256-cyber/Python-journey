#Q1:Store following word meanings in a python dictionary :
# Table : “a piece of furniture”,data : “List of facts & figures”,cat : “a small animal”
word_meaning ={'Table': 'a piece of furniture',
               'data' : 'list of facts & figures',
               'cat': 'a small animal'}
print(word_meaning)
print(type(word_meaning))

#Q2:You are given a list of subjects for students. Assume one classroom is required for 1 subject. 
# How many classrooms are needed by all students. 
# ”python”“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

subject=["python","java","C++","python”","javascript","java","python","java","C++","C"]
unique_subject=set(subject)
print("Number of classes needed for unique subject:",len(unique_subject))

#Q3:WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}
x=float(input("ENTER NUMBER OF MATHS:"))
marks.update({"Maths":x})
z=float(input("ENTER NUMBER OF Physics:"))
marks.update({"Physics":z})
y=float(input("ENTER NUMBER OF Chemistry:"))
marks.update({"Chemistry":y})
print(marks)
#Q4:Figure out a way to store 9 & 9.0 as separate values in the set.
set={(9,"int"),(9.0,"float")}
print(set)

# Q5:Create two sets:
# Find:Union,Intersection
set1={1,2,3,5,8,9,7}
set2={1,2,4,6}
print(set1.intersection(set2))
print(set1.union(set2))

#Q6:Merge two dictionaries:
d1={"day":"Saturday", "date":21}
d2={"month":3,"Year":2026}
d1.update(d2)
print(d1)
