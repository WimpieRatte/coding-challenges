from random import randint
die1 = randint(1, 6)
die2 = randint(1, 6)
die3 = randint(1, 6)
print(die1)
print(die2)
print(die3)

if die1 % 2 == 0 and die2 % 2 == 0 and die3 % 2 == 0:
    print("You have 3 even numbers")
elif die1 % 2 != 0 and die2 % 2 != 0 and die3 % 2 != 0:
    print("You have 3 odd numbers")
    
if die1 == die2 and die2 == die3:
    print("Three of a kind!!!")
elif die1 == die2 or die2 == die3 or die1 == die3:
    print("1 Pair!!!")
else:
    print("Better luck next time!")