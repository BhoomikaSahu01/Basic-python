''' while loop

count = 1
while count <= 5:
    
    print("hello")
    count += 1
    
print(count)

#print numbers from 1 to 5
i = 100
while i >= 1:
    print(i)
    i-=1
print("loop ended")

# print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
    
# print number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
    
# print the multiplication table of a number n
n = int(input('enter n number'))
i = 1
while  i <= 10:
    print(n * i)
    i += 1
    
# print the elements of the following list using a loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
movies = ["ready", "3idiot", "adventure", "bawaal"]

idx = 0
while idx < len(movies):
    print(movies[idx]) # numbers of index
    idx += 1
    
    
# search of a number x in this tuple using loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )

x = 36
i = 0 #initialization
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    
    i += 1  
    

largest_number = -99999999

#input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# if the number is not equal to -1, continue

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input('enter the number or type -1 to stop:'))
    
print("The largest number is: , largest_number")'''

'''write a program that reads a sequence of numbers and counts how many
 are even and how many are odd. the program terminate when zero is entered

odd_numbers = 0
even_numbers = 0

number = int(input("Enter a number or type 0 to stop:"))
while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("enter a number or type 0 to stop:"))
    
print("odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

i = 0
while i <= 10:
    print(i)
    i += 1
    
i = 10
while i >= 1:
    print(i)
    i -= 1

i = 2
while i <= 20:
    print(i)
    i += 2
    
i = 1
while i <= 19:
    print(i)
    i += 2
    
i = 1

while i <= 20:
    print(i)
    i += 2'
    
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("sum =", total

num = int(input("enter a number:"))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
    
print("Factorial=",fact)

count = 2
while count <= 20:
    print(count)
    count += 2
    
i = 1
sum =0 
while i <= 100:
    sum += i
    print(i)
    i += 1
print("sum =", sum)

no = int(input("enter a number"))
i = 1
while i <= 10:
    num = i * no
    print(num)
    i = i + 1
    
num = int(input('enter a number'))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("fact =",fact)

num = int(input('enter a digit:'))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits =", count)

num = int(input('enter a number :'))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
    
print("Reverse =", reverse)

num = int(input("enter a number:"))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    
if original == reverse:
    print("palindrome")
else:
    print("Not palindrome")'''
    

    





 
    

     

    
    

    