#Tuple
#A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


#Create tuple
fruits = ('Apples','Oranges','Grapes')
#fruits2 = tuple(('Apples','Oranges','Grapes'))


#Single value needs trailing comma
fruits2 = ('Apples',)


#Get a value
print(fruits[1])


#Can't change value
#fruits[0] = 'Pears'


#Delete tuple
del fruits2
#print(fruits2) – NameError: name 'fruits2' is not defined


#Get length
print(len(fruits))



#Sets
#A Set is a collection which is unordered and unindexed. No duplicate members.

#Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}


#Check if in set
print('Apples' in fruits_set)


#Add to set
fruits_set.add('Grape')
print(fruits_set)

#   Duplicates are ignored
fruits_set.add('Grape')
print(fruits_set)

#Remove from set
fruits_set.remove("Grape")
print(fruits_set)

#Clear set - Set is still there, just nothing is in it
fruits_set.clear()
print(fruits_set)

#Delete set
del fruits_set
#print(fruits_set) - NameError: name 'fruits_set' is not defined
