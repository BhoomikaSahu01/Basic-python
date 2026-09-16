# Dictionaries
'''marks = {"harry" : 34, "jack": 45, "lily":94}

#print(marks, type(marks))
print(marks["lily"])

marks["harry"] = 3
print(marks)

# Method in Dictionary
marks = {"harry": 34, "jack": 45, "lily":94}

print(marks.keys())
print(marks.values())
#marks.clear()
marks.pop("lily")
print(marks)'''

#Dictionary comprehension
table_of_5 = {i: 5*i for i in range(1, 11)}
print(table_of_5)