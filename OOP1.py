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



