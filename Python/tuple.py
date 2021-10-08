#tuple is ordered and unchangeble and allow duplicate values
#unchangeable means we cannot change, add or remove items after creating
thistuple = ('hello', 'apple', 'banana', 11, True)  #can contain members of multiple data types
print(thistuple)
print(len(thistuple))

singleItemTuple = ('item',) #add , because python wont know if it is a tuple
print(type(thistuple))

'''tuples are unchangeable, but if you want to change its values, you can change it to 
list, make changes, and convert it back to tuple'''
y = list(thistuple)
y.append('lion')
thistuple = tuple(y)
del y
print(thistuple)

#you are allowed to add tuples to tuples.
y = ('chirag',)
thistuple += y
print(thistuple)

#join two tuples 
z = thistuple + y
#you can also multiply tuples
z = y * 4
print(z)

#you cannot delete items from tuple directly, but you can delete the tuple itself

del y #deletes the tuple

'''packing and unpacking. Packing is creating a tuple. unpacking is extracting values back into variables'''
(x,y,z,a,b,c,d) = thistuple #unpacking. Note: no of variable must match the num of items
print(x,y,z,a,b,c,d)
(a,b,*c) = thistuple #adding * makes the last element as list and takes values of the remaining elements
print(a,b,c)


#METHODS

#count() : returns the number of times a value appears. Syntax: tuple.count(value)
print(thistuple.count('chirag'))

#index() : returns the index of value
print(thistuple.index('chirag'))
