# Patterns
# star patterns
'''for row in range(1,6):
    print("* " * 5)
    
for row in range(1,6):
    print("* " * row)
  
n = 3  
for row in range(1, n+1):
    print("* " * (n-row+1))
    
n = 5
for row in range(1, n+1):
    print(""*(row - 1)+ "* " *(n-row+1))'''

#known as row wise pattern
# n = 5
# for row in range(1, n+1):
#     print(" "*(n-1)+"* "*(n-row+1))
# for row in range(1, n+1):
#     print(" "*(n-row)+"* "*(row))
# for row in range(1, n+1):
#     print("* "*2*n)
    
# coloumn wise pattern
# n = 5
# for row in range(1, n+1):
#     print("* "*row+" "*(2*(n-row))+"* "*row)
# for row in range(1, n+1):
#     print("* "*(n-row)+"  "*(2*(row))+ "* "*(n-row))


# how a covert a number in binary
# no = 123456789
# while no != 0:
#     digit = no % 10
#     print(digit)
#     no = no // 10
    
# no = 5
# bi = " "
# while no != 0:
#     bit = no % 2
#     bi = bi + str(bit)
#     no = no // 2
    
# print(bi[::-1])

#Haming Distance

