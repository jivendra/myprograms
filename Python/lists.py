thislist = ['apple', 'banana', 12, False]  #list items can be of any type
print(thislist)
#Properties : ordered, changeble, allow duplicate
thislist[1] = 'Pineapple'
print(thislist)

print(len(thislist))

print(type(thislist)) #From Python's perspective, lists are defined as objects with the data type 'list'

#check is the item exists
if 'apple' in thislist:
    print('Apple is present')

#insert items insert(position, value)
thislist.insert(1,'mango')
print(thislist)

#use append to add items to the end
thislist.append('cheeku')
print(thislist)

#to concatenate a list to another, use entend. It can also append tuples, set and dictionary to list
newlist = ['audi', 'bmw']
thislist.extend(newlist) #this adds newlist to the end of thislist
print(thislist)

#looping over
[print(x) for x in thislist]
#Removing
thislist.remove('audi')
print(thislist)
thislist.pop() #removes the last element
print(thislist)
thislist.pop(0) #removes the specified index
del thislist[0] #also rmoves the specified index
print(thislist)
thislist.clear() #empties the list
print(thislist)
del thislist #deletes the list

#list apprehention
thislist = [x for x in newlist]
thislist.clear()
thislist = [x.upper() for x in newlist]
thislist.sort() #sort the list , this is case sensitive, capital letters will be placed before
thislist.sort(key=str.lower) #case-insensitive sort
thislist.sort(reverse=True) #sort the list in descending order
print(thislist)

thislist.reverse() #reverses the list without any sorting

#copy a list
thislistcopy = thislist.copy() #we cannot do thislistcopy = thislist, as it will be a reference to the
                               #same list and any changes made to one list will reflect to another\
del thislistcopy
thislistcopy = list(thislist) #another method to make a copy
list3 = thislist + thislist #Join two list
print(list3)

#append a whole list to another list
thislist.extend([x for x in range(3)])
print(thislist)
