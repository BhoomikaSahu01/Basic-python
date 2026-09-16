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

'''Inheritance'''

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

    