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

