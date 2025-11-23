# Conditional Statements
'''
age = 21
if age >= 18 :
    print("You can vote");
'''

'''
age = int(input("Enter your age: "))
if age >= 18 :
    print("You can vote");
else:
    print("You can't vote")
'''

'''
color = input("Enter color: ")

if color == "red":
    print("Stop");
elif color == "green":
    print("Go");
elif color == "yellow":
    print("Look");
else:
    print("wrong color")
'''

'''
age = int(input("Enter your age: "))

if age < 13:
    print("Child");
elif (age < 18 and age > 13):
    print("Teenager");
elif age >= 18:
    print("Adult");

else:
    print("Wrong input") 

    '''

# Login 


'''
name = input("Enter your name: ")
passd = input("Enter the password: ")

user_name = "admin"
password = "pass"

if (name == user_name and passd == password):
    print("Welcome user");
elif (name != user_name):
    print("Wrong user name");
else:
    print("Wrong password")
    '''

# multiple of 5
'''
num = int(input("Enter the number: "))

if(num % 5 == 0):
    print(num , " is the multiple of 5");
else:
    print(num , " is not the multiple of 5")
'''
# odd or even 
'''
num = int(input("Enter a number: "))
if(num <= 0):
    print("Invalid number");
elif(num % 2 == 0):
    print(num , " is an even number");
else:
    print(num , " is an odd number")
    '''

# Match case

'''
color = input("Enter the color: ")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("Default case wrong")
        '''
