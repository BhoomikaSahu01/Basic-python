'''
# find sum of two numbers
a = 40
b = 55
sum = a+b
print(sum)

# find Quotient and Remainder
a = 10
b = 25
a, b = b, a
print(a)
print(b)

# Calculate the Area of a Rectangle
a = 10
b = 5
quatient = a//b
remainder = a % b
print("quatient =", quatient)
print("remainder =", remainder)

# Area of rectangle
a = 10
b = 55
area = a * b
print(area)

# calculate area of a circle
radius = 6
circle = 3.14*radius*radius
print("area of circle =",circle)

# Find the square and Cube of a Number
num = int(input("enter a number"))
square = num ** 2
cube = num ** 3
print("square =",square)
print("cube =",cube)'''

''' Check whether a Number is Even or Odd
num = int(input("enter a num:"))
if(num % 2 == 0):
    print("even number")
else:
    print("odd number")
    
# calculate simple interest
r = 55
p = 22
t = 88
SIP = (r * p * t)/ 100
print(SIP)
# calculate average of Three Numbers
a = 77
b = 88
c = 99
average = (a+b+c)/3
print(average)

# Reverse the Digits of a Three-Digit Number
num = int(input("enter a number:"))
r1 = num % 10
q1 = num // 10
r2 = q1 % 10
q2 = q1 // 10
r3 = q2 % 10
print("reverse of 3 n0 :",r1,r2,r3)'''

'''Find the last digit of the number
num = 9876
last = num % 10
print(last)


# Find the first digit of a Number
num = 9876

while num >= 10:
    num = num // 10
print(num)

#check if a Number is Divisible by 5 and 11
num = 55
if num % 5 ==0 and num % 11 == 0:
    print("num is divisible")
else:
    print("not divisible")
    
# convert total days into years, weeks, and Days
days = 500

years = days//365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print("Years =",years)
print("weeks =",weeks)
print("remaining_days=", remaining_days)

#Find the power of a Number
base = 2
exponent = 5
print(base ** exponent)


# Comparision Operator
# check if two numbers are equal
a = int(input("enter first no :"))
b = int(input("enter two no :"))

if a == b:
    print("equal numbers")
else:
    print("not equal no")


# Find the largest of two numbers
a = int(input("enter the no:"))
b = int(input("enter the no :"))
 
if a > b:
    print("no a is greater")
elif a < b:
    print("no b is greater:")
else:
    print("a is equal to b")
    
#Logical Operater(and, or, not)

#check voting eligibility
age = int(input("enter the age:"))

if age >= 18:
    print("adult")
else:
    print("not adult")
    
#Check if a number lies between 10 and 50
num = int(input('enter a number:'))

if num >= 10 and num <= 50:
    print("number lies bet 10 and 50")
else:
    print("number not lies ")
    
# username and password validation

username = input("enter username:")
password = int(input("enter password"))

if username == "nancy" and password == 1234:
     print("Login successful")
else:
    ("invalid credentials ")
    
#Assignment Operater(+= ,-=. *=, /=, //=, %=, **=)

#incerease salary by 10 percent
 
salary = 30000

salary += salary * 0.10 # salary = salary + (salary * 0.10)
print(salary)

# Add bonus to marks
marks = 70

marks += 5
print(marks)

# Bitwise Operator (&,|,^,~,<<,>>)

# Check if a number is even using bitwise operator
num = int(input("enter a number:"))

if num & 1:
    print("Odd")
else:
    print("Even")
    
# Multiply a number by 4 using left shift
num = int(input("Enter a number:"))
print(num << 2)

# Divide a number by 2 using right shift
num = int(input("Enter a number:"))
print(num >> 1)'

# Membership Operators(in, not in)
text = "python"
ch = input("Enter a character:")

if ch in text:
    print("present")
else:
    print("Not present")
    
# check if an item exists in a list
numbers = [10, 20, 30, 40]

num = int(input("Enter a number: "))

if num in numbers:
    print("Found")
else:
    print("Not Found")
    
#Identity Operators(is, is not)
# check if two variables refer to the same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

#Check if a variable is None
value = None

if value is None:
    print("Value is None")
else:
    print("Value is not None")

# Conditional (Ternary) operator

# Find the greater number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = a if a > b else b

print("Largest =", largest)

# Relational Operator

a = 50
b = 20
print(a == b)
print(a != b)
print( a >= b)
print(a <= b)
print(a < b)


# assignment operators
num = 10
num = num + 10
num += 10
print("num =",num)

# Logical operators
a = 50
b = 20
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)

a = 50
b = 30
print("OR operator:", (a == b) or (a > b))

# Type Conversion

a = 2
b = 4.25
sum = a + b
print(sum)

a , b = 1 , "2"
c = int(b)
sum = a + c

a = 3.14
a = str(a)
print(type(a))

name = input("enter your name:")
print("Welcome", name)

int = ("5")
val = int(input("enter some value: "))
print(type(val), val)

# Write a program to input 2 numbers and print their sum
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
sum = num1 + num2
print("sum =",sum)

# WAP to input side of a square and print its area
side = int(input("side of a square"))
area = side * side
print("area =", area)

# WAP to input 2 floating point numbers and print their average
num1 = float(input("enter no:"))
num2 = float(input("enter no:"))
average = num1 + num2 / 2
print("average=",average)

#WAP to input 2 int numbers, a and b
#print True if a is greater than or equal to b. if not print False

a = int(input("enter a no:"))
b = int(input("enter a no:"))
print( a >= b)'''






