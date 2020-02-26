# A List is a collection which is ordered and changeable. Allows duplicate members.


#Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples','Oranges','Grapes','Pears']


#Use a constructor
#numbers2 = list([1,2,3,4,5])

#print one specific position
print(fruits[1])

#Get length
print(len(fruits))

#Append to list
fruits.append("Mangos")

#Remove from list
fruits.remove('Grapes')

#Insert into position
fruits.insert(2,'Strawberries')

print('Inserted \'strawberries\' into fruits. Before and after pop(): \n')
print(fruits)

#Remove with pop
fruits.pop(2)
print(fruits)

#Change a position
fruits[0] = 'Blueberries'

#Reverse List
fruits.reverse()

#Sort list
fruits.sort()




print(fruits)