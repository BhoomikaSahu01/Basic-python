'''# gassing a number and win price

a = int(input("enter a number between 1 and 10:"))

match a:
    case 1:
        print("you won a charger")
    case 3:
        print("you won $3")
    case 6:
        print("you won a camera")
    case _:
        print("Better luck next time")

# for loop
for i in range(1, 6):
    print(i)
    
for i in range(1, 11):
    print("5 * ",i , " = ", 5*(i))
    
prices = [100, 600, 150]
total = 0

for price in prices:
    total += price
    
print("Total Bill =",total)'''
        