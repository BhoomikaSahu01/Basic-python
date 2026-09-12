# Strings
'''str1 = "This is a string.\nwe are creating it in python."
print(str1)
str2 = 'ApnaCollege'
str3 = """this is a string"""

'this is apnacollege"s tutorial'


str1 = "apna"
str2 = "college"
final_str = str1 + str2
print(final_str)

# length of string len(str)
str1 = "apna"
len1 = len(str1)
print(len1)
str2 = "college"
final_str = str1 + str2
print(final_str)

# indexing
name = "Nancy"
print(name[0])
print(name[1])
print(name[2])

# name = " H  a  r  r  y"
#index =   0  1  2  3  4
#-index=  -5 -4 -3 -2 -1

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4]) #(5-4)=1 name[1]
print(name[-5])

# string slicing and indexing
name = "Harry"
print(name[0:2])# goes from 0 to 2-1 means 0 to 1
print(name[1: 4])
print(name[2:-1])# same as name [2:4]

name = "Harry0123456789"
#print(name[0:10:n]) #skip n-1 char

print(name[0:10:1])# skip 0 character
print(name[0:10:2])# skip 1 char output Hry13
print(name[:4])#harr replace first emptynum with 0
print(name[1:])# arry0123456replace the second empty num the len


# string methods and function
name = "Harry" #strings are immutable
#name[0] = "R" #you cannot do this
a = len(name)
print(a)#5

# common string method
s = "hello world nancy"
a = len(s)
print(a)
print(s.upper())# upper is a function  makes capital
print(s.lower())#lower case
print(s.capitalize()) # first words of the string willbe capitalize
print(s.title())# they both the first word capitalize

text = "hello world"
print(text.strip())# "hello world"
print(text.lstrip())#"hello world  "
print(text.rstrip())#"  hello world"

# Finding and Replacing
text = "python is fun"
print(text.find("is")) #output 7 7 idexing per is hain idex of first occurance
print(text.replace("fun", "awesome"))# python is awesome


#splitting and joining
text = "Apples,Bananas,Pineapples"
print(text.split(",")) # 'Apples','bananas','pineapples'
print(",".join(['Apples','bananas','pineapples']))

# Checking String properties
text = "python123"
print(text.isalpha())#output : false
print(text.isdigit())#output :false
print(text.isalnum())#output: True alpha numeric string
print(text.isspace())#output: False'''

# string formatting and f - strings
'''
template = ''Dear {}, You are awesome.Take this {}$ bag''
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s1 = template.format(a, a1)
print(s1)'''

# f string
template = '''Dear {}, You are awesome.Take this {}$ bag'''
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

print(f"dear {a} you are awesome and take this {a1}$ bag")

#Note please mainly use f string avoid using formats
# ASCII american standard code for information interchange


