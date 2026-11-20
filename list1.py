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




