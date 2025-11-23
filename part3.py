# Slicing in String  Strings is immutable
'''
str = "Python"
print(str[2:4])
'''

# String Fromatting
'''
a = 10
b = 20

print(f"sum of {a} and {b} is {a+b}")
'''

# List Datatypes
# it is mutable
'''
marks = [99,98,97,96,95,"Sujal",7.55,True]
print(marks[2])
print(len(marks))
'''

# List Methods
'''
num = [1,2,3]
num.append(4)  #add value at the last
num.insert(2,200) # 2 is index num and 200 is value
# num.sort() # sort in incresing order
# num.sort(reverse=True) # sort in decreasing order
num.reverse() # reverse the whole list
print(num)
'''

'''
val = [1,2,3,4,5]
x = 4
idx = 0
for i in val:
    if(i == x):
        print(f"{x} is in index {idx}")
        break
    idx +=1
    '''
    
# tuples datatypes
# it is immutable
'''
tup = (1,2,3,4,5)
sum = 0
for i in tup:
    sum+=i

print(f"The sum of {tup} is {sum}")
'''

# Dictionary Datatypes
# it is mutable
# No duplicate keys
# unordered DT

'''
student = {
    "name": "Sujal",
    "Dept" : "BCA",
    "reg" : "222"
}
student["Dept"] = "BMLT" # assigning new value
print(student)
print(student.keys()) # prints all the key value
print(list(student.items())) # typecasting to list type of all dict items
print(student["reg"])
'''

 
# Sets Datatypes
# it is mutable
# unordered

'''
empty_set = set() # creating empty set
values = {1,2,3,4,5,5,2}
print(values)
'''
# Set Methods

'''
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}
s = s1.union(s2)
s_it = s1.intersection(s2)
print(s)
print(s_it)
'''

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

'''
unique_courses = set()
for i in info:
    if(i[1] == "English"):
        print(i[0])

    # unique_courses.add(i[1])
    # print(i[1])

# print(unique_courses)
'''

dict = {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({name : set() })
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)