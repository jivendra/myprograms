#Dictionary is used to store data in key: pair values
#It is changeble, does not allow duplicates, ordered(since pyton 3.7)
thisdict = {
    'brand': 'ford',
    'model': 'Mustang',
    'year': 2012
}
print(thisdict)
print(thisdict['year'])

#dictionary length
print(len(thisdict))

#print keys
print(thisdict.keys())

#print values
print(thisdict.values())

print(thisdict.items())

#changing values

thisdict['model'] = 'figo'
thisdict.update({'model': 'aspire'})

#adding values
thisdict['color'] = 'red'
thisdict['Wheel'] = 'alloy'

#removing values
thisdict.pop('color') #pass the key to pop function

thisdict.popitem() #this will delete the last item inserted

del thisdict['year'] # deletes the item of specified key

print(thisdict)

#looping
for x in thisdict:
    print(x) # this will print the keys

for x in thisdict:
    print(thisdict[x]) #this will print the values

for x,y in thisdict.items():
    print(x,y) #loop through both key and value

#copying dictionary
newdict = thisdict.copy()
newdict2 = dict(thisdict)  #these are the two ways to copy dictionary

#Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
