"""
Dict
"""

# spam = {'name': 'Zophie', 'age': 7}
# print(spam['name'])

"""
dict programm - birthday - input 
"""
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name) # birthdays[name] your printing the key. from the value that you inputted and was alredy inside the dict
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
print ("---------------------------------------")
"""
dict program for loops 
"""
spam = {"color": "red", "age": 42}

for i in spam.values(): # print all values
    print(i)

for k in spam.keys(): # print all keys
    print(k)

for items in spam.items(): # print all items
    print(items)

print(list(spam.items())) # in place dict to list

for k, v in spam.items():
    print("Key :"+ k +"Value :"+str(v))

print( "-----------------------------------------------")
"""
checking whether a key or value exists in a dict 
"""

spam1 = {"name": "zophie","age": 7}

print("name" in spam1.keys())

print("zophie" in spam1.values())

print("color" in spam1.keys())

print ( " ------------------------------------------------")

"""
Get method = It’s tedious to check whether a key exists in a dictionary before accessing that key’s value. Fortunately, 
dictionaries have a get() method that takes two arguments: 
the key of the value to retrieve and a fallback value to return if that key does not exist.
"""

picnicItems = {"apples": 5, "cups": 2}
print("im bringing " + str(picnicItems.get("cups",0))+ " cups")
print("im bringing " + str(picnicItems.get("eggs",0))+ " eggs")
print("----------------------------------------------------------------")
"""
setdeault () Method = The first argument passed to the method is the key to check for, and the second argument is 
the value to set at that key if the key does not exist. If the key does exist, the setdefault() method returns the key’s value.

"""

spam2 = {"name": "pooka","age": 5}

print(spam2.setdefault("color","black"))

print ( spam2)

print(spam2.setdefault("color","white"))  # it will not work. it will still return white because there's alredy in the dict a color - black

print ( spam2)


print ("-----------------------------")
"""
count over the number of letters iterations - using setdefault 
"""
message = " This is me Daniel Leyghton I'm studying currently, thank you very much."

count = {}

for i in message:
    count.setdefault(i,0)
    count[i] = count[i]+1
print ( count)

print ( " *******************************************")

"""
Pretty printing 

"""
import pprint

message = " This is me Daniel Leyghton I'm studying currently, thank you very much."

count = {}

for i in message:
    count.setdefault(i,0)
    count[i] = count[i]+1
pprint.pprint( count)


