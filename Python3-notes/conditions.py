#Conditions
#If/Else conditions are used to decide to do something based on whether or not the condition is true or false

x = 10
y = 20

#Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#if x > y:
#    print(f'{x} is greater than {y}')
#elif x == y:
#    print(f'{x} is equal to {y}')
#else:
#    print(f'{y} is greater than {x}')



#Nested if
#if x > 2:
#    if x <= 10:
#        print(f'{x} is greater than 2 and less than or equal to 10')




#Logical operators (and, or, not) - Used to combine conditional statements

#if x > 2 and x <= 10:
#    print(f'{x} is greater than 2 and less then or equal to 10')
    
#if x > 2 or x <= 10:
#    print(f'{x} is greater than 2 or less then or equal to 10')

#if not(x == y):
#    print(f'{x} is not equal to {y}')



#Membership operators (not, not in) - Membership operators are used to test if a sequence is presented in an object.

#numbers = [1,2,3,4,5]

#if x in numbers:
#    print(x in numbers)
    
#if x not in numbers:
#    print(x not in numbers)


#Identity Operators (is, is not) – Compare the object (not if they are equal) but if they are actually the same object with the same memory location.

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)