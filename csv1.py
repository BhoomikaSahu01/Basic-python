f = open("data.txt", "r")
data = f.read()
print(data)
print(type(data))


#read multiple line
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

f.close()

#write krne ki method
f = open("data.txt","w")
f.write("I want to learn javascript tomorrow")
f.close()
