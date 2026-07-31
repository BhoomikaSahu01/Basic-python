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
        
maximum(25,50,40)'''

# Function to Reverse a String
def reverse_string(name):
    result = ""
    for ch in name:
        result = ch + result
        print(result)
        
reverse_string("BhoomikaSahu")
        
    
    






