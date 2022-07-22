## Day 3 Lesson
## Conditionals and Loops pt.2
## Putting it all together into
## FizzBuzz!

print("Below is an example of creating an if statement with an alternate case")
print("This is the same as saying 'If something is TRUE, do this, if FALSE, do something else'")
print("i.e. If a+b = 4, print 'Hello World!', otherwise, print 'Goodbye World!'")
print("We can try an example of this below: ")

input("Hit enter to continue: ")

a = 2
b = 2

if(a+b == 4):
    print("Hello World! Block 1")
else:
    print("Goodbye World! Block 2")

input("Hit enter to continue: ")

print("You can take the if-else conditions further by creating a near unlimited amount of conditions")
print("To achieve this, we use the command 'elif()', which represents 'else if...'")
print("Below is another example: ")

input("Hit enter to continue: ")

if(a == 0):
    print("Variable 'a' is 0 | Block 1")
elif(a == 1):
    print("Variable 'a' is 1 | Block 2")
elif(a == 2):
    print("Variable 'a' is 2 | Block 3")
else:
    print("Variable 'a' is greater than 2 | Block 4")

input("Hit enter to continue: ")

## Try playing around with variables a and b to see how they work

## Note that elif is the same as if, it just continues to check other conditions
## when it realizes the previous condition wasn't TRUE. Above we can see that when 
## variable 'a' IS NOT EQUAL TO 0, it checks if it is equal to 1. If it IS NOT EQUAL TO 1, 
## then it checks if variable 'a' is equal to 2. Eventually if it runs out of conditions
## it will stop checking, and the final block (Block 4) will run. This else statement tells
## the program "if all the checks above were FALSE, then run this final block". If the 
## else statement is not included, and no conditions are satisfied, the program
## will end without printing anything. 


## For today's assignment, you will utilize variables, for-loops, and conditionals
## to create the FizzBuzz program. FizzBuzz is a program that loops through a fixed
## number and prints out each number. If the number is a multiple of 3, the program
## prints "Fizz" instead. If the number is a multiple of 5, it prints "Buzz" instead.
## If the number is a multiple of both 3 AND 5, print "FizzBuzz".

## Solution:

## Modify this variable to change how many numbers it runs to
loops = 30

for x in range(loops):
    if(x%3==0 and x%5==0):      # What is being used here is called a "modulus" operator.
        print("FizzBuzz")       # Similar to division, it returns the REMAINDER of a division operations.
    elif(x%3==0):               # i.e. 6/3 = 2, 6%3 = 0, 
        print("Fizz")           # 7/3 = 2 and 1 remainder, 7%3 = 1.
    elif(x%5==0):
        print("Buzz")
    else:
        print(x)


