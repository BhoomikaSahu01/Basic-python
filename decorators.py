#Decorater is a function that takes a function, it creates a new
#function a new function
'''
def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper


def say_hello():
    print("Hello !")
    
#say_hello()
f = decorator(say_hello)
f()

#Using decorators with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for_ in range(n):
                func(a)
        return wrapper
    return decorator

repeat(3)'''
'''Decorator is a function that takes a function, it
creates a new function inside its body(wrapper) then
it returns that new function

def decorator(func): # function is an argument
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
        
    return wrapper
@decorator
def say_hello():
    print("Hello !")
    
say_hello() # both things you  can try
#f = decorator(say_hello)
# # f()
'''
'''
 f will look something like this
def f():
    print("I am about to execute a function...")
    print("Hello!")
    print("I have executed this function..")


'''
# Using Decorators with Arguments
# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator

# @repeat(7)
# def say_hello(a):
#     print(f"Hello ! {a}")
    
# say_hello("Harry")
    
'''
It replaces the function say_hello with this:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
        return wrapper
    
'''

'''Create a decorator that prints a message before 
executing a function

def my_decorator(func):
    def wrapper():
        print("function is starting")
        func()
    return wrapper

@my_decorator
def hello():
    print("Hello world")
    
hello()
'''

'''create a decorator that print a message after
a function executes


def my_decorator(func):
    def wrapper():
        func()
        print("funciton is completed")
        
    return wrapper


@my_decorator

def display():
    print("welcome to python")

display()'''

'''Create a decorator that counts how many times
a function is called

def count_calls(func):
    count = 0
    
    def wrapper():
        nonlocal count
        count += 1
        print("call number:", count)
        return func()
    
    return wrapper

@count_calls
def greet():
    print("Hello")
    
greet()
greet()
greet()'''

'''create a decorator that works with 
function arguments

def my_decorator(func);
    def wrapper(*args, **kwargs):
        print("Executing function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a,b):
    print(a + b)
    
add(10,20)'''

# def  my_decorator(func):
#     def wrapper():
#         print("something is happening before the function is call")
#         func()
#         print("something is happening after the function is call")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello !")
    
# say_hello()
        
'''Using Decorators with Arguments'''
# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for _ in range(n):
#                 func(a)
#             return wrapper
#         return decorator
    
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")

# Chaining Multiple Decorators

# def uppercase(func):
#     def wrapper():
#         return func().upper()
#     return wrapper

# def exclaim(func):
#     def wrapper():
#         return func() + "!!!"
#     return wrapper

# @uppercase
# @exclaim
# def greet():
#     return "hello"
# print(greet())
    
# def decorator(func):
#     def wrapper():
#         print("Transaction initiated")
#         func()
#         print("Transaction completed")
#     return wrapper

# def hello():
#     print("...Executing all steps of Transaction...")
    
# hello1 = decorator(hello)
# hello1()

# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("after function")
#     return wrapper


# def greet():
#     print("Hello!")
 
# greet1 = decorator(greet)   
# greet1()
        
        
# def decorator(func):
#     def inner(a, b):
#         print("{0} and {1} are the two numbers this function will add".format(a,b))
#         print("The summation of {0} and {1} is".format(a,b), end =" ")
        
#         if a < 0 or b < 0:
#             print("Number cannot be negative")
#             return
#         return func(a,b)
#     return inner

# @decorator    
# def summation(a,b):
#     return a+b

# if __name__ == '__main__':
#     print(summation(6,7))
    
            
# Add two numbers using a decorator
# def decorator(func):
#     def inner(a, b):
#         print("Numbers", a, b)
#         return func(a, b)
#     return inner

# @decorator
# def add(a, b):
#     return a + b

# print(add(10, 20))

#multiple Decorator

def decor1(func):
    def inner():
       return func().upper() #shantanu kejkar
    return inner

def decor2(func):
    def inner():
        return func().split()
    return inner
@decor2
@decor1

def get_name():
    name = input("enter first name")  #shantanu
    sirname = input("enter sirname")   #kejkar
    full_name = name + " "+ sirname
    return full_name

get_name = decor2(decor1(get_name))
print(get_name())

#decor1: - shantanu kejkar
#decor2: - ["shantanu","kejkar"]


    

    



        


