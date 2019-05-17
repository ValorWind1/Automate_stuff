"""
apend will add arguments to the ned of list.

The insert() method can insert a value at any index in the list. The first argument to insert()
is the index for the new value, and the second argument is the new value to be inserted.
"""

spam = ['cat', 'dog', 'bat']
# print( spam.append('moose'))

spam.insert(1,"chicken")
print(spam)

"""
The append() and insert() methods are list methods and can be called only on list values,
 not on other values such as strings or integers.
"""

# REMOVING VALUES FORM LIST REMOVE ()

spam.remove("bat")
print(spam)

"""
however if multiple of same values it will only remove the first one. 
del() is good to used when we know the index of an item. 

"""

#SORTING VALUES IN A LIST SORT()

spam1 = [2, 5, 3.14, 1, -7]
spam1.sort()
print(spam1)

#reverse order

spam1.sort(reverse=True)
print(spam1)

# SORTING USES ASCIIBETICAL order not actual alphabetical order

spam2 = ['a', 'z', 'A', 'Z']
spam2.sort(key=str.lower) # key = str.lower = sorting in alphabetical order otherwise,
print(spam2)

spam2.sort()
print(spam2)