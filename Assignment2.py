# Q1

'''
def tax_rate (n) :
    if (n < 30000):
        print("Tax deduct of 5%")
        n/=5
        print(n)

    elif(n > 30000 and n < 70000):
        print("Tax deduct of 15%")
        n/=15
        print(n)

    elif(n > 70000):
        print("tax deduct of 25%")
        n/=25
        print(n)



tax_rate(25000)

'''

# Prime number
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n% i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if (is_prime(num)):
    print(num," is a prime number")
else:
    print(num," is not a prime number")

    '''

# sum of digits

'''
def sum_of_digits(n):
    sum = 0
    for i in range(n+1):
        sum+=i
        i+=1
    return(sum)

print(sum_of_digits(20))

'''

# divisiblity test for 5 and 3

'''
def devisibility_test():
    for i in range(100):
        if(i%3 == 0 and i % 5 == 0):
            print(i)

devisibility_test()
'''