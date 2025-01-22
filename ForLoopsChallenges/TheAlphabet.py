# Using the ASCII code to display letters of the alphabet
print(chr(65))  # A
print(chr(66))  # B
print(chr(67))  # C

results = ""
for i in range(65, 91):
    results += chr(i)
    
print(results)