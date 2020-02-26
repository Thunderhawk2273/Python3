#Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods.

name = 'Will'
age = 24

#Concatenate
#print('Hello, my name is ' + name + ' and I am ' + str(age))


#String Formatting


#Arguements by position
#print('My name is {name} and I am {age}.'.format(name=name, age=age))

#F-Strings (v3.6+)
#print(f'Hello! My name is {name}, and I am {age}.')

#String Methods

s = "hello world"
print(f'The string we are using is \"{s}\".')
#Capitalize string
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lower
print(s.lower())

#swapcase
print(s.swapcase())

#Get length
print(len(s))

#Replace
print(s.replace('world', 'everyone'))

#Count
sub = 'h'
print(s.count(sub))

#Starts with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find position
print(s.find('r'))

#Is all aplhanumeric
print(s.isalnum())

#Is all alphabetic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())