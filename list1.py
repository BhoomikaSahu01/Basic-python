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