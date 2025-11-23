# Palindrome check
'''
def is_palindrome():
    val = input("Enter a word: ")
    reverse_str = val[::-1]
    if(val == reverse_str):
        print(f"{val} is palindrome")
    else:
        print(f"{val} is not palindrome")


is_palindrome()
'''

'''
list = [1,2,3,4,5,6,7,8]
sum = 0
for i in list:
    sum+= i

avg = sum/len(list)
print(avg)
'''

'''
def merge_list():
    
    values = list(map(int, input("Enter the list ").split()))
    values2 = list(map(int, input("Enter the list ").split()))
    values.extend(values2)
    values.sort()
    print(values)

merge_list()
'''