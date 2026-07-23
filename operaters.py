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
print(base ** exponent)'''