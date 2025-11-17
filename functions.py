# Sum function

'''
def sum(a,b):
    sum = a+b
    return sum

print(sum(1,2))
'''

# Average Function
'''
def avg(a,b,c):
    average = (a+b+c)/3
    return average

print(avg(2,4,6))

'''

# Lambda Function

'''
sum = lambda a,b: a+b
print(sum(1,2))
'''

# Factorial calculation

'''
def calc_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact


print(calc_factorial(3))
'''

# Q2

'''
def calc_Even(a,b):
    for i in range(a,b):
        if(i % 2 == 0):
            print(i)
            

a = int(input("Enter the first number : "))
b = int(input("Enter the second number: "))

calc_Even(a,b)
'''