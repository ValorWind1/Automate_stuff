import os

"""
creating new folders 
"""
# os.makedirs(" write your path here ")

"""
Finding file sizes and folder contents 
"""
#os.path.getsize(path) = will return the size in bytes of the file in the path
print(os.path.getsize("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff"))

# os.listdir(path) = will return a list of filename strings for each file in the path
print(os.listdir("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff"))


# finding total size of all files in a directory
# use os.path.getsize() , and os.listdir()
totalsize = 0
for i in os.listdir("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff"):
    totalsize = totalsize + os.path.getsize(os.path.join("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff"))
print(totalsize)


"""
checking path validity (if the path exist or not )
"""
#os.path.exists(path) = will returh true if the file/folder exists , false otherwise

#os.path.isfile(path) = will return true if path exist , and is a file

#os.path,isdir(path) = return true if path exists and is a folder

#ex

print(os.path.exists("C:\\Windows"))

print(os.path.exists("C:\\fake_news_make_up_folder"))

# checking if there's USB connected , and named D:/

print(os.path.exists("D:\\"))

"""
saving variables with shelve module 
"""

import shelve
shelf_file = shelve.open("mydata")
cats = ["Zophie","Pooka","Simon"]
shelf_file["cats"] = cats
shelf_file.close()

# opening and checking data was stored correctly
shelf_file = shelve.open("mydata")
print(type(shelf_file))
print(shelf_file["cats"])
shelf_file.close()


"""
saving variables with pprint.pformat() function 
"""
# saving a dict to another py file from here . using pprint
import pprint
cats = [{"name":"Zophie","desc":"chubby"},{"name":"Pooka","desc":"fluffy"}]
print(pprint.pformat(cats))
file_object = open("myCats.py","w")
print(file_object.write("cats=" + pprint.pformat(cats)+"\n"))
file_object.close()

#from the generate python program lets do something with it.
import myCats
myCats.cats
print(myCats.cats[0])
print(myCats.cats[0]["name"])