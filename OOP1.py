'''Class : Class is a blueprint or a template. Eg. Form for an
Exam that contains name, age, electives, father's name etc

#Object: Specific instance created from the template(class.).Eg. Form which 
contains the data for John Doe
'''
'''
class Employee:
    company = "HP"
    
    def get_salary(self):# self is important here because self is a way to reference
        #the object of the class which is being created
        print(self)
        return 34000
    
e = Employee() # An object of class Employyee is created here
print(e.get_salary()) #Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)'''

'''constructor

class Employee:
    def __init__(self, salary, name, bond):# this is use for constructor
        self.salary = salary # Create an instance attribueof name
        #salary and assign it with salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. salary is {self.salary}.The bond is for {self.bond} years")
    
e1 = Employee(34000, "John Doe", 4)
#print(e1.get_salary())
e1.get_info()'''

'''Inheritance

class Animal: #parent class (superclass)
    def __init__(self, name):
        location = "Australia"
        self.name = name
    def speak(self):
        print("Generic animal sound")
        
class Dog(Animal): #This is how inheritance is done in python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof!")
    
        
#a = Animal("Dog")
#a.speak()

d = Dog("Bruno")
d.speak()
print(d.location)

# instance of a class
class Employee:
    company = "Asus" #This is class attributee
    
    def __init__(self, salary, name, bond, company):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company
        
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. salary is {self.salary}.The bond is for {self.bond} years")

e1 = Employee(3400, "John", 3, "Tesla")
print(e1.company)# will always print instance attribute whenever present
print(Employee.company)# This will always print the class attribute

# Object introspection
print(dir(e1))  '''

'''inheritance and polymorphism

class Animal: # parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic animal sound")
        
class Dog(Animal): # This is how inheritance is done in python
    def speak(self):
        super().speak()# We are using the speak function of the parent class
        print("Woof !")
        
# a = Animal("Dog")
# a.speak() 
d = Dog("Bruno")
d.speak()
print(d.location)'''

'''# Method overiding and overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
        
p1 = Point(3, 2)
p2 = Point(6, 3)

p = p1.sum(p2) # Returns a new point which is sum of p1 and p2




class Point:
    
        
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")
        
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))
        
p1 = Point(3, 2)
p2 = Point(6, 3)

#p = p1.sum(p2) # Returns a new point which is sum of p1 and p2
p = p1 + p2 # we overloaded the +operator by writting __add__ function
p.print_point()'''



'''classes and object
class dog: # we define a class "dog"
    species = "canis familiars"# A class attribute(shared by a)
    
def __init__(self, name, breed):
    self.name = name
    self.breed = breed 
    
def bark(self):
    print(f"{self.name} says woof!") # A method (an action the dog can do)
    
# Now, let's create some dog objects:
my_dog = dog("Buddy", "Golden Retriever")'''

# creating class
# class Student:
    
#     def __init__(self, name, marks, section): # Making constructor automatically invoke
#         self.name = name
#         self.marks = marks
#         self.section = section
#         print("adding new student in Database")
    
    
# # creating object(instance)

# s1 = Student("karan", 97, "A") # class name
# print(s1.name, s1.marks, s1.section) #karan

# s2 = Student("arjun", 98, "B")
# print(s2.name, s2.marks, s2.section)


# # print(s1.name)

# s2 = Student()
# print(s2.name)

'''# we are making factory for producing a Class

#this is how a class is created
class Car:
    color = "blue"
    brand = "mercedes"
 
# this is how an object is created   
car1 = Car()
print(car1.color)
print(car1.brand)

class Student:
    
    college_name = "ABC college"
    
    name = "anonymous" #class attribute
    
    #default constructors
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self, name, marks, section): # Making constructor automatically invoke
        self.name = name #obj attribute obj attribute ki preference class attribute se hire hoti hain
        self.marks = marks
        self.section = section
        print("adding new student in Database")
    
    
# creating object(instance)

# s1 = Student("karan", 97, "A") # class name
# print(s1.name, s1.marks, s1.section) #karan

# s2 = Student("arjun", 98, "B")
# print(s2.name, s2.marks, s2.section)

# print(Student.college_name)

s1 = Student("karan", 97)
print(s1.name)'''
#Method
# Methods a
# re functions that belongs to objects

'''class Student: # classes
    college_name = "ABC College"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome():
        print("welcome student,", self.name)
        
    def get_marks(self):
        return self.marks
        
s1 = Student("karan", 97) #object
print(s1.name)
print(s1.get_marks())
        
        
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is", sum/3)
        
        
s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()
s1.name

# Static Methods
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod # convert a function into static method  
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is", sum/3)
        
        
s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()
s1.name

class Student:
    @staticmethod  #decorator
    def college():
        print("ABC College")
        
class Car:
    # Constructor
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
     
     #methof   
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")
        
    # object
car1 = Car()
car1.start()'''

'''Let's practice
Create Account class with 2 attributes - balance & account no.
create methods for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance=", self.get_balance)
        
    # Credited method
    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("total balance=", self.get_balance)
                    
            
    #function for return the balance
    def get_balance(self):
        return self.balance
            
        
        
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(90000)
acc1.credit(10000)
acc1.debit(10000)


# del keyword

class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("shraddha")

print(s1.name)  
del s1.name
print(s1.name)

#Private(like) attributes and methods
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.acc_pass)

class Person:
    __name = "anonymous"
    
    def __hello(self):
        print("hello person !")
        
    def welcome(self):
        self.__hello()
    
p1 = Person()
print(p1.welcome())'''

'''Classes ane objects

class Dog:
    species = "Canis Familaries" # Class attribue
    
def __init__(self, name, breed):# constructor
    self.name = name #instance attribute
    self.breed = breed # instance attribute
    
# Method
def bark(self):
    print(f"{self.name} says woof!")
    
#Object
first_dog = Dog("buddy", "golden retriever")
another_dog = Dog("lucky", "labrador")

# We can access their attributes

print(first_dog.name)
print(another_dog.breed)

# we can perfor action
first_dog.bark() # buddy says woof
print(Dog.species) # Canis Familiars'''

'''Create a student class with name and age. Display the details

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 = Student("Bhoomika",22)
print(s1.name , s1.age)'''

'''create an employee class with name and salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
emp1 = Employee("kirtan", 10000)
print("Name =", emp1.name)
print("salary =", emp1.salary )'''

'''Create a car class with a start() method
class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print(self.brand, "is starting")
        
car1 = Car("Toyota")

print(car1.brand)
car1.start()'''

'''Create a calculator class and two numbers

class Calculater:
    def add(self, a, b):
        return a + b
    
c = Calculater()

result = c.add(10, 20)
print("sum:", result)'''

'''Create a class to calculate the area of a rectangle

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        print("area of rectangle =", self.length * self.breadth)
area_ofR = Rectangle(10,20)

print(area_ofR.length, area_ofR.breadth)
area_ofR.area()'''

'''create a class that checks whether a number
is even or odd

class Number:
    def __init__(self, num):
        self.num = num
        
        
    def even_odd(self):
        if self.num % 2 == 0:
            print("even")
        else:
            print("odd")
            
n = Number(55)
n.even_odd()'''

'''create a Student class that checks whether the 
student passed or failed

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        
    def pass_fail(self):
        if self.marks >= 40:
            print("pass")
        else:
            print("fail")
            
s1 = Student("nancy", 78)
print(s1.name, s1.marks)

s2 = Student("shiv", 88)
print(s2.name, s2.marks)

s1.pass_fail()
s2.pass_fail()'''

'''calculate an employee's annual salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def annual(self):
        self.salary = self.salary * 12
        print ("annual salary",self.salary)
        
emp1 =Employee("raghav", 10000)
print(emp1.name, emp1.salary)
emp1.annual()'''

'''create a calculator using a class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
c = Calculator()

print("addition:", c.add(10, 5))
print("substraction:", c.subtract(10,5))
print("multiplication:",c.multiply(10, 5))
print("Division:", c.divide(10,5))'''
    
''' Create a bank account with deposit and withdrawl

class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance= self.balance + amount
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
            
    def show_balance(self):
        print("Balance:", self.balance)
        
account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)

account.show_balance()'''
    
    


    
    
            


    
        
        
        
    
    

    
    
    

    


        





     



