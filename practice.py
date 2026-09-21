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
but does nothing for numbers 3(use pass)
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
            print(5)'''
            
'''create a string variable name with your fullname. Print
 1 the first char
 2 the last char
 3 the length of the string
 
Name = "Bhoomika Sahu"
print(Name[0])
print(Name[-1])
print(len(Name))'''

'''Concatenate two strings "hello" and "world"
 with a space in between

name = "hello" + " " + "world"
print(name)# we also do with str1 and str2 (str1,str2)
 '''
 
#string slicing and Indexing
''' Given text = "python programming", do the following
1 print the first 6 characters
2 print the last 6 characters
3 print every second character from the string

text = "python programming"
print(text[0:6])
print(text[-6:])
print(len(text))
print(text[::2])'''

'''reverse the string text using slicing
text = "python programming"
print(text[::-1])'''

'''Take the string "i love python programming" and:
1. Remove extra spaces from both ends
2. Convert it to little case
3. count how many times "o" appears

text = " i love python programming "
print(text.strip())
print(text.title())
print(text.count("o"))'''

'''Check if the string "123abc" is alphanumeric
  
str1 = "123abc"
#print(str1.isalpha()) # it is  an alphanumeric string

if str1.isalnum():
    print("yes this string is alphanumeric")
else:
    print("this string is not alphanumeric")'''
    
#String Formatting and f-Strings
'''Using format(), create a sentence:
"My name is John and I am 25 years Old."
by passing "John" and 25 as variables.

name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")
  
name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name,age)) 

   '''
   
#String Manipulation challenges
'''
1 Given sentence = "Coding in python is fun", replace 
"fun" with "awesome" and print it.
2 find the index of the word "python" in sentence.
3 Convert the entire sentence to uppercase and print it

sentence = "Coding in python is fun"
new = sentence.replace("fun", "awesome")
print(new)'''

'''Find the index of the word "python" in sentence.
sentence = "coding in python is fun"
ind = sentence.index("python")
print(ind)'''

'''Convert the entire sentence to uppercase and print it
    
sentence = "coding in python is fun" 
print(sentence.upper())'''

'''1. write a program  that counts how many vowels are in
a given string
2. Take a user input string and check if it is a palin
drome (same forwards and backwards)

sentence = "Coding in python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in sentence:
     if(char in vowels):
        sum += 1
        
print(f"There are {sum} vowels in this sentence")'''

# membership operators

'''check whether an element exits in a list
list = [10,20,30,40,50]


if 20 in list:
    print("element is present")
else:
    print("not present")'''
    
''' Check whether a charcter is present in a string 
char = ["A","B","C","D"]

if "A" in char:
    print("True")
else:
    print("false")'''
    
# not in
''' write a python program to check whether 25 is not present
in a list

num = [67,89,65,44]

if 25 not in num:
    print("25 is not present")
else:
    print("25 is present")'''
    
'''Check whether a character is not present in a string
word = "python"
if "z" not in word:
    print("False")
else:
    print("True")'''
    
'''Given two lists, print the elements of the first list
that are absent from the second list

list1 = [5, 6, 7, 8]
list2 = [1, 2, 3, 4]

for num in list1:
    if num not in list2:
        print(num)'''
        
'''Remove duplicate numbers from a list without using set()

numbers = [10, 20, 10, 30, 20, 40]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)'''

'''write a function greet() that prints "Hello, Python Learner!"
 when called
def greet():
    print("Hello, Python Learner!")
    
greet()'''

'''Write a function square(num) that returns the square
of a given number.Test it with different numbers.

def square(x):
    return x * x
print(square(3))
print(square(5))
print(square(2))'''

'''Write a function full_name(first, last) that takes first
name and last name as parameters and return a single
string in the format "First Last" 

def full_name(first, last):
    return f"{first} {last}"
print(full_name("John","Doe"))
'''

'''write a function calculate_area(length, width=10)
that returns the area of a rectangle.Test it by calling
the function with
1 Both length and width
2 Only length(use default width)

def calculate_area(length, width = 10):
    return length * width

print(f "The area of the rectangle is {calculate_area(13, 20)}")
print(calculate_area(13))'''

'''check whether two variables refers to the same object
a = [10, 20, 30]
b = a
print(a is b)'''

'''Check two separate list
a = [10, 20, 30]
b = [10, 20, 30]
print(a is b)
print(b is a)'''

'''using is not
x = [1, 2, 3]
y = [1, 2, 3]

if x is not y:
    print("They are different object")
else:
    print("They are the same objects")'''
    
'''identity operator with None

name = None
if name is None:
    print("no name provided")'''
    
'''Function returning the same object
def get_data():
    data = [10, 20, 30]
    return data

a = get_data()
b = a
print(a is b)'''

'''Check two seperate lists'''
a = [10, 20, 30]
b = [10]



    


     

        
    


    


    