'''# functions
def calc_sum(a,b):# a and b parameters
    sum = a + b
    print(sum)
    return sum

calc_sum(2,3) # 2 and 3 are arguments
calc_sum(7,8)
calc_sum(9,10)

# function defination
def calc_sum(a,b):
    return a + b

sum = calc_sum(2,3) # function call; arguments
print(sum)

# print Hello
def print_Hello():
    print("Hello")
    
print_Hello()

# average of three numbers
def average(a, b, c):
    sum = (a+b+c)/3
    print(sum)
    return sum

average(3,4,5)
average(40,50,60)

# WAF to print the length of a list
cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)

#WAF to print the elements of a list in a single line


cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_list(list):
    for item in list:
        print(item , end = " ") #item end is used for nect like \n
   
print_list(heroes)
print()
print_list(cities)

# Write to find the factorial of n.(n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(6)

# WAP to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD=", inr_val, "INR")
    
converter(1)

# Write a function to add two numbers

def add_numbers(a, b):
    sum = a + b
    print(sum)
    
add_numbers(5,6)
add_numbers(9,10)

# Write a function to check whether a number is even or odd

def even_Odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

even_Odd(9)
even_Odd(10)

# Write a function to find the maximum of three numbers
def maximum(a,b,c):
    if a >= b and  a>=c:
        print("a is greater")
    elif b >= c:
        print("b is greater")
    else:
        print("c is greater")
        
maximum(25,50,40)

# Function to Reverse a String
def reverse_string(name):
    result = ""
    for ch in name:
        result = ch + result
        print(result)
        
reverse_string("BhoomikaSahu")

def add(a,b):
    return  a + b

sum = add(3, 4)
print(sum)'''

'''check even or odd
def even_odd(num):
    if(num % 2 == 0):
        return "even"
    else:
        return "odd"
    
#sum = even_odd(7)
#print(sum)

print(even_odd(8))'''

'''Find square of a number
def square(num):
    sum = num * num
    return sum

print(square(9))'''

'''Find maximum of two numbers
def maximum(a,b):
    if(a > b):
        return "a is greater than b"
    else:
        return "b is greater than a"
        
print(maximum(8,9))'''

'''Check positive and negative
def pos_neg(num):
    if num >= 0:
        return "num is positive"
    else:
        return "num is negative"
    
print(pos_neg(-7))'''

'''calculate factorial
def factorial(num):
    result = 1
    
    for i in range(1, num + 1):
        result *= i
        
        return result
    print(factorial(5))'''
    
'''Find the largest of two numbers
def largest(a,b):
    if a > b:
        return " a is greater than b"
    else:
        return "b is greater than a"
    
two = largest(8,9)
print(two)'''

'''check positive negative or zero
def Pos_neg_zero(num):
    if num > 0:
        return "positive"
    elif num == 0:
        return "zero"
    else:
        return "Negative"
    
print(Pos_neg_zero(-9))'''

'''find factorial
# def factorial(num):
#     result = 1
#     for i in range(1, num + 1):
#         result = result * i # 1*1*2*3*4*5*6*7*8
#         return result
    
# print(factorial(8))

def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result

print(factorial(5))'''

'''Reverse a string
def reverse(num):
    return num[::-1]

print(reverse("hello"))

# count vowels in a string
def count_vowels(text):
    count = 0
    
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
            
    return count
print(count_vowels("hello"))

# Find the maximum number in a list
def find_max(numbers):
    maximum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
            
    return maximum
print(find_max([10, 25, 7, 40, 15]))

# Check whether a number is prime
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
print(is_prime(7))'''
        
        
        
        
    
    
        

        
    
    






