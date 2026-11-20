class queue: #create a class
    def __init__(self):
        self.values = [] #initialize an empty list
    def enqueue(self, x): #enquee method
        self.values.append(x)
    def dequeue(self): #Remove an element
        front = self.values[0]
        self.values = self.values[1 :]
        return front
    
q1 = queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print(q1.values)
q1.enqueue(40)
print(q1.values)
print(q1.dequeue())
print(q1.values)