# print("Hello \n Sujal")

# Varibles 
'''
name = "Sujal"
age = 21
PI = 3.14
isPRime = True
isNotPRime = None '''

# print("name,age,PI")

# Data Types  in Python
'''
name = "Sujal"
age = 21
PI = 3.14
isPRime = True
isNotPRime = None

print(type(name))
print(type(isPRime))
'''

# caculate sum of 2 numbers 
'''
num_1 = 10
num_2 = 20
sum = num_1+num_2
print(sum)
'''
# Logical Operator
'''
print(13 > 12 and 2 < 10)   
print(not (20 ==10))
print (1==1 or 20>30)
'''

'''
x = 3
x += 5
print(x)
'''

# Type Casting & Type conversion
'''
sum = 5 + 10.2 # Type conversion
sum2 = int(5 + 10.4) # type casting
print(type(sum))
print(type(sum2))
'''

'''
num = input("Enter a number: ")
print(num)
'''

# Average of two numbers

'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
average = int((num1 + num2) / 2)
print(average)
'''

# Q1
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello ",name,"you are ", age ," old")

'''

# Q2
'''
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 % num_2)
'''

# Q3
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = float(input("Enter the third number: "))

average = float((a + b + c)/3)
print(average , type(average))
'''

# Q4
'''
var = input("Enter the number 45: ")
int_var = int(var)
float_var = float(var)
print(var, type(var))
print(var, type(int_var))
print(var, type(float_var))
'''

# Q5
'''
x = 10+3+2**2
print(x)
'''

# Q6
'''
val1 = int(input("Enter the first number: "))
val2 = int(input("Enter the second value: "))
val1,val2 = val2,val1
print(val1,val2)
'''

# Q7
'''
Celcius = float(input("Enter the value: "))
Fahrenheit_temp = (Celcius * (9/5)) + 32
print(Fahrenheit_temp)
'''

# Q8
'''
radius = float(input("Enter the radius value: "))
pi = 3.14

area = pi * radius**2
print(area)

'''

# Q9
'''
p = float(input("Enter the value: "))
r = float(input("Enter the value: "))
t = float(input("Enter the value: "))
SI = (p*r*t)/100
print(SI)
'''

# Q10
'''
num = input("Enter a float number: ")
int_part , frac_part = num.split(".")

print(int_part,frac_part)
'''