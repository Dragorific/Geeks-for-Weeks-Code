# Whole numbers
a = 15 
b = 20

# Strings
x = "Hello "
y = "World."

# Fractional Numbers
d = 1.5

# Combination of whole and fractionals
c = a + b + d

# Booleans
varOne = True
varTwo = False

print(a + b + d == c)
if (a + b + d == c):
    print("Yes, this statement is valid")
    d = 5.5
    varOne = False
    varTwo = True

print(varTwo)
if (varTwo):
    print("varTwo is True")

# Combination of whole and fractionals
c = a + b + d

# Loops
# range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 10) = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for a in range(1,11):
    print(a*5)

# Housing retail prices
varList = [400, 450, 800, 700, 1100, 1800]

# Program to check if a house worth 800k exists
for b in varList:
    if b == 800:
        print("Yes there is a house worth 800k")

a = 800
i = 0.025

# While loop to determine when a house price 
# reaches 1mil with an inflationary rate of 2.5%
while(a < 1000):
    a = a*(1 + i)
    print("House price this year:", a) # Ctrl + C to stop infinite loop
    



    