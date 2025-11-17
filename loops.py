# Loops Concept

'''
num = 1 # iterator
while num <=5:
    print(num,"Hello Sujal")
    num +=1

    '''

'''
i = 5
while (i>=1):
    print(i)
    i-=1

    '''

# Multiplication Table

'''
num = int(input("Enter a number: "))
j = num
i = 0

while (i < 13):
    print(j , " * " ,i, " = " ,j* i )
    i+=1

    '''

# Break and Continue

'''
i = 1
while (i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i+=1
'''
'''
i = 1
while(i <= 10):
    if( i % 3 == 0):
        i+=1
        continue
    print(i)
    i+=1

'''

# Printing all odd number from 1 to 20 

'''

i = 1
while (i <20):
    i+=1
    if(i%2 == 0):
        
        continue
    print(i)
   
'''

# For loop
'''
str = "Sujal Thapa"
for i in str:
    print(i)
'''

'''
count = 0
word = "Sujal"
for i in word:
    count+=1

print(count)
'''

# Vowel count

'''
word = "sujal"
vowels = "aeiou"
count = 0
for i in word:
    for j in vowels:
        if(i == j):
            count+=1

print(count)
'''

# Sum of n numbers

'''
num = int(input("Enter a number: "))
sum = 0
for i in range(num+1):
    sum+=i

print(sum)

'''