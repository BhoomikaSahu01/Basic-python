'''def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1 # it creates local variable called z
    return c


def greet():
    z = 32 #Local variable
    print("Hello")
    
z = 8 #z is a global variable
print(z)
print(sum(4, 6))
print(z)

def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z # Please modify global z
    z = 0 # this will refer to global z and not create a local variable
    return c
z = 3
print(sum(3, 12))
print(z)'''

# DocStrings
def sum(a,b):
    '''This will sum two numbers'''
    c = a + b
    return c

print(sum.__doc__)

