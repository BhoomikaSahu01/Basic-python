'''marks = [54, 23, 64, 93, 32]
mixed = [43, "Hello", False, 4.2]

print(marks[2:4])
print(mixed[2])
print(mixed[4])# error index out of bound

marks = [5, 2, 21, 5, 7]

marks.append(63)#This will change the original list
print(marks)
marks.pop(2) # index no pop
print(marks)

# extend method join to list
marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

marks.extend(extra_marks)
print(marks)

# Create a list containing the table of 5

a = 5
table = []

for i in range(1, 11):
    table.append(5 * i)
print(table)'''

#list comprehension
'''table of 5

table = [5*i for i in range(1, 11)]
print(table)'''

''' Create numbers from 1 to 10
numbers = [x for x in range(1, 11)]
print(numbers)'''

'''create even numbers from 1 to 20
even = [x for x in range(1, 21) if x % 2 == 0]
print(even)'''

'''create odd numbers from 1 to 20
odd = [x for x in range(1,21) if x%2 != 0]
print(odd)'''

'''Find squares from 1 to 10
squares = [x ** 2 for x in range(1,11)]
print(squares)'''

marks = [4, 5, 6, 8]
# print(marks)
# print("length =" ,len(marks))
# print(type(marks))

# print(marks[:5])
# print(marks[1:2])
# print(marks[1:])
# print(marks[-3:-1])
#marks = [4, 5, 6, 8]
#marks.append(9)
#marks.sort(reverse=True)
#marks.insert(0,8)
#marks.pop(0)
#marks.remove(5)
#marks.reverse()
#print(marks)

# '''list comprehension'''
# square = [x**2 for x in range(5)]
# print(square)

# '''find the largest element of the list'''
# list = [10, 20, 40, 50]

# largest = list[0]

# for i in list:
#     if i > largest:
#         largest = i
        
# print(largest)

'''wap to ask the user to enter names of their 3 favorite movies and store them in a list
movies = []
mov1 = input("enter first mov:")
mov2 = input("enter second mov:")
mov3 = input("enter third mov:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)'''

'''wap to check if a list contain a palindrome of elements
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
    '''
    
'''store the above values in a list and sort them from "A" to "D"
list = ["a", "z", "a", "d", "b"]
list.sort()
print(list)'''

'''create a list fuits = ["apple", "banana", "cherry"]
1 print the first fruit
2 replace "banana" with orange
3 print the length of the list

list = ["apple", "banana", "cherry"]
print(list[0])
print(len(list))
list[1] = "orange"
print(list)'''

''' start with numbers = [5, 2, 9, 1, 7]
1 sort the list in ascending order
2 append the number 10 to the list
3 remove the number 2 from the list

numbers = [5, 2, 9, 1, 7]
numbers.sort()
numbers.append(10)
numbers.remove(2)
print(numbers)'''

'''find the sum of all elements
marks = [5, 2, 9, 1, 7]
#print(len(numbers))
sum = 0
for i in marks:
    sum = sum + i
    
print(sum)'''

'''find the largest element in a list
marks = [5, 8, 9, 99, 44]

largest = marks[0]
for i in marks:
    if i > largest:
        largest = i
        
print(largest)'''

'''find the smallest element in a list
marks = [10, 20, 30, 40, 50]
smallest = marks[0]

for i in marks:
    if i < smallest:
        smallest = i
        
print(smallest)'''

'''sort the list in ascending order
marks = [5, 2, 21, 5, 7]
marks.sort()
print(marks)'''

'''sort the list in decending order
marks = [5, 2, 21, 5, 7]
marks.sort(reverse = True)
print(marks)'''

'''reverse a list
marks = [5, 2, 21, 5, 7]
marks.reverse()
print(marks)'''

'''count how many times an element appears
marks =[5, 2, 5, 7, 5, 8]

print(marks.count(5))'''

'''Remove duplicate elements from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)'''

'''find even number from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = [x for x in numbers if x%2 == 0]
print(even)'''

'''find odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd = [x for x in numbers if x%2 != 0]
print(odd)'''

'''find squares of all elements
numbers = [1, 2, 3, 4, 5]
square = [x**2 for x in numbers]
print(square)
'''

'''separate positive and negative numbers
numbers = [10, -5, 20, -3, 0, 8]
positive =[x for x in numbers if x > 0]
negative =[x for x in numbers if x < 0]
print(positive)
print(negative)'''

'''Merge two lists
list1 = [5, 5, 8, 9]
list2 = [7, 9, 10, 18]
list3 = list1 + list2
print(list3)'''


'''check whether an element exists in a list
numbers = [10, 20, 30, 40]
if 30 in numbers:
    print("element found")
else:
    print("element not found")'''
    
'''find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]
print(common)'''

'''check whether a list is palindrome
list = [1, 2, 1]
copy_list = list.copy
copy_list.reverse()

if copy_list == list:
    print("palindrome")
else:
    print("not palindrome")'''
    
'''find the second smallest element
numbers = [10, 20, 5, 40, 30]
numbers.sort()
print(numbers[1])'''

'''move all zeros to the end of a list
numbers = [0, 1, 0, 3, 12]
new_list = []
for i in numbers:
    if i != 0:
        new_list.append(i)
print(new_list)'''

'''find the frequency of each element
numbers = [1, 2, 2, 3, 3, 3, 4]

for i in numbers:
    if numbers.index(i) == numbers.index(i):
        print(i, "=", numbers.count(i))'''
        
'''
numbers = [1, 2, 2, 3, 3, 3, 4]

for i in numbers:
    if i not in []:
        pass

frequency = {}

for i in numbers:
    frequency[i] = frequency.get(i, 0) + 1

print(frequency)'''

        








