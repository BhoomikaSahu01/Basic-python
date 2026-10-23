'''class stack: # create a class
    def __init__(self): # initialize empty list
        self.values = [] # store stack element
    def push(self, x):
        self.values = [x] + self.values
    def pop(self):
            return self.values.pop(0)
        
s = stack()
s.push(10) # 10
s.push(20) #20, 10
s.push(30) # 30, 20, 10
s.push(40) # 40, 30, 20, 10

print(s.values) # 40, 30, 20, 10
print(s.pop())
print(s.values)
s.push(60)
print(s.values) # 60, 30, 20, 10
print(s.pop()) # pop 60'''

# create a stack with push(), pop(), and display() method
class Stack: # create a class
    def __init__(self):
        self.values = []
        
    def push(self, x): #method
        self.values.append(x)
        
    def pop(self): #mehtod
        if not self.values:
            return "stack is empty"
        return self.values.pop()
    
    def display(self):
        print(self.values)
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()
print(s.pop())
s.display()
    