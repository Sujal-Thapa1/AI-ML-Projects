'''
class Student:
    subject = "Python"
    college = "ABC"
    year = "4th Year"


stu1 = Student()
print(stu1.subject)
'''

# class Student:
#     def __init__(self):
#         pass

'''
class Student:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name


# stu1 = Student("Sujal")
# print(stu1.name)
stu = Student("Sujal")
print(stu.get_name())
'''

# Types of Constructor
# 1: Default constructor and Parameterized constructor
'''

def is_palindrome():
    value = input("Enter a word: ").lower()
    reverse_value = value[::-1]
    if(value == reverse_value):
        print(f"{value} is  a palindrome")
    else:
        print(f"{value} is not a palindrome")
    

is_palindrome()
'''

'''
list1 = list(map(int,input("Enter a list: ").split()))
list2 = list(map(int, input("Enter list 2: ").split()))
new_list = list1 + list2
new_list.sort()
print(new_list)
'''

'''
list1 = [1,2,3,5,6,7]
list2 = [1,2,3,6,8,9,7,9]
new_list = []
for i in list1:
    for j in list2:
        if(i == j):  
            new_list.insert(i,j)
            # print(f"{list1} common element = {list1}")
print(new_list)
'''
