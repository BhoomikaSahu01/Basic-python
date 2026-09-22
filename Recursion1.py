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
    
show(5) # 5, 4= n-1, 3= n-2, 2= n-3, 1'''
    