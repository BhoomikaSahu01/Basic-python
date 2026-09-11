'''# create a program that checks if a person is eligible to vote(age >= 18)
age = int(input("enter age:"))
if (age >= 18):
    print("eligible for vote")
else:
    print("they can not vote")'''
    
'''write a program that takes a number
from the user and prints "even" if it is
 even otherwise "Odd" 
 
num = int(input("enter a number:"))
if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")'''
    
''' Ask the user the enter day number(1-7) and 
print the corresponding day of the week using 
match case

day = int(input("enter a (1-7) day:"))

match day:
    case 1:
        print("monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")'''
        
'''write a program using match case that simulates
a simple calculator

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

operation = (input("choose operation:"))
match operation:
    case "+":
        print(num1 + num2)
        
    case "-":
        print(num1 - num2)
        
    case "*":
        print(num1 * num2)
        
    case "/":
        print(num1 / num2)'''
        
''' print numbers from 1 to 10 using a for loop

for i in range(1, 11):
    print(i)'''
    
    
'''print the multiplication table of a number

n = int(input("enter a number"))
for i in range(1, 11):
    print(n, "X" , i, "=", n * i)'''
    
'''calculate the sum of all numbers from 1 to 100
using a for loop

sum = 0
for i in range(1, 101):
    print(i)
    sum += i
    
print(sum)'''

'''print the pattern using the for loop

for i in range(1, 5):
    print("*" * i)'''
    
'''print numbers form 1 to 10 using a while loop
i = 1
while i < 11:
    print(i)
    i = i + 1'''
    
'''sum of 1 to 100 in while loop
sum = 0 
i = 1
while i <= 100:
    sum += i
    i = i + 1
print(sum)'''

'''write a program that keeps asking the user to enter
a  password until they enter the correct one
password = "y2k123"
entered_pass = input("enter password:")

while(entered_pass != password):
    entered_pass = input("wrong password! Try again and enter password")
    
print("Success ! you are logged in")'''

'''use a whileloop to reverse a given number
num = 45222

print(int(str(num)[::-1]))'''

''' use a for loop to print numbers from 1 to 10,
but stop the loop if the number is 7

for i in range(1, 11):
    
    if i == 7:
        break
    print(i)'''
        
'''print numbers from 1 to 10 , skipping the
number 5
for i in range(1,11):
    
    if i == 5:
        continue
    print(i)'''
    
'''Write a loop that goes through numbers 1 to 5,
but does nothing for numbers 3(use pass)'''
for i in range(1, 6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)
    
  
    
    
         


    