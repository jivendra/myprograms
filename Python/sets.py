'''Sets are is unordered and unindexed and do not allow duplicate values'''
thisset = {'giraffe', 'lion', 'chirag', True}

for x in thisset:
    print(x, end=' ')
print()

#you can add new items to sets
thisset.add('india')

#you can one set to another
set2 = {'item2', 'item1'}
set2.update(thisset)  # this does not have to be a set, it can be list, tuple, or dictionary
                    # this will add items of thisset into set2. It will exclude duplicate items

for x in set2:
    print(x, end=' ')
print()

#remove items
thisset.remove(True)
for x in thisset:
    print(x, end=' ')
print()

'''discard items: the difference between this and remove() is if item does not exist, remove will raise error and 
 discard will not'''

thisset.discard('giraffe')

#pop: this will remove any random item from list because sets are unordered
thisset.pop()
for x in thisset:
    print(x, end=' ')
print()

#delete the set completely: del
del set2


