# function

'''#function defining
def average(a ,b ,c):
    d = (a+b+c)/3
    print(d)
    
#function calling
average(3 ,5 ,1)
average(4, 2, 1)

# Another Way
def average(a ,b ,c):
    d = (a+b+c)/3
    return d
    
#function calling
o1 = average(3 ,5 ,1)
o2 = average(4, 2, 1)

print(o1)
print(o2)

# arguments
def add(a, b):
    x =  a + b
    return x

c = add(3, 5)
print(c)

# type of arguments
# positional arguments

# Default arguments

def add(a, b, plus=0):
    x = a + b + plus
    return x

c = add(3, 5, 2)
print(c)

# keyword Arguments
def add(a, b):
    x = a + b
    return x

c1 = add(a=5, b=6)''''

# Lambda Function in python

square = lambda x: x * x

'''As good as writing
def square(x):
    return x * x
'''

sum = lambda x, y: x + y
'''
As good as writing
def sum(x, y):
    return x + y
'''

print(square(3))
print(sum(3, 62))


    
    