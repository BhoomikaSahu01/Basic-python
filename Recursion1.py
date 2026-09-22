'''# Recursion
def show(n):
    if(n == 0): # Base case
        return
    print(n)
    show(n - 1)
show(5)'''

# search fibonacchi series
''' 0 1 1 2 3 5 8 13
ind 0 1 2 3 4 5 6 7 ...

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n - 2) + fib(n - 1)


def fib(n):
    # Base case of recursion
    if(n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1)
print(fib(6))

fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1'''

#Recursion
'''When a function call itself repeatedly


def show(n):
    if(n == 0): # Base case
        return
    print(n)
    show(n-1)
    

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
show(5) # 5, 4= n-1, 3= n-2, 2= n-3, 1

def show(n):
    if n==0 :
        return
    print(n)
    show(n-1)
    
show(9)'''

'''print numbers from 1 to N
def print_num(n):
    if n == 0:
        return
    print_num(n-1)
    print(n)
    
print_num(9)'''

'''print numbers from N to 1
def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n-1)
    
print_num(8)'''

'''print "Hello" N times
def hello(n):
    if n == 0:
        return
    print("hello")
    hello(n - 1)
    
hello(9)'''

'''Find Sum From 1 to N
def total(n):
    if n == 0:
        return 0
    return n + total(n-1)

print(total(5))

def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)
print(total(5))'''

'''find factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))'''

'''print even numbers from 2 to N
def even_numbers(n):
    if n < 2:
        return
    
    even_numbers(n - 1)
    
    if n % 2 == 0:
        print(n)
        
even_numbers(6)

def even_number(n):
    if n < 2: # base case of recussion
        return
    even_number(n - 1) # recursive call
    
    if n % 2 == 0:
        print(n)

even_number(10)'''

'''Print odd numbers from 1 to N
def odd(n):
    if n < 1:
        return
    odd(n -1)
    if n % 2 != 0:
        print(n)
odd(10)'''

'''Find a power of a number with recursion code
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)
print(power(2, 5))

def power(a,n):
    if n == 0:
        return 1
    return a * power(a, n-1)

print(power(2, 5))

def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)
    print("End")
    
show(3)'''
     

    
    
        
    

    
    