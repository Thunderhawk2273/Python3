#A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


#Create function - Sam is default if nothing is given as an arguement
def sayHello(name = 'Sam'):
    print(f"Hello {name}")
    

sayHello()
sayHello('John Doe')


#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total
    

num = getSum(3,4)
print(num)



#A lambda function is a small anonymous function.
#A lambda function can take any number of arguements, but can only have one expression. Very similar to JS arrow functions

getM = lambda num1, num2: num1 * num2

print(getM(8,5))

