#Iterative Sum for number 5
sum = 0
for i in range(1,6): 
   sum = sum + i
print("Iterative Sum for 5 = " + str(sum))

sum = 0
x = int(input("Give a number: "))
for i in range(1,x+1): 
   sum = sum + i
print(f"Iterative Sum for {x} = {sum}")