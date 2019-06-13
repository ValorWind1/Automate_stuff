"""
import shutil = mofule functio lets us copy,move,rename,and delete file in your python program

"""

# copying files
"""
shutil.copy (source,destination)
"""
import shutil , os
# os.chdir("C:\\")
# shutil.copy("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\04-11-1994.txt","C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\other_folder")
# shutil.copy("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\test2.txt","C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\other_folder\\changing_test2_name.txt")
#❶, the original spam.txt filename is used for the new, copied file’s filename. The second shutil.copy() call ❷ also copies the file at


#copying folder , and every folder and file contained in it
"""
shutil.copytree()
"""
# os.chdir("C:\\")
# #The shutil.copytree() call creates a new folder named other_backup with the same content as the original other folder.
# shutil.copytree("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\other_folder","C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\other_folder_backup")


#moving and renaming files and folders
"""
shutil.move. will move the file/folder at the destination provided. 
program will be on a different py file 
"""
# shutil.move('C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\move.txt', 'C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\other_folder_backup')



# permantly deleting files and folders
"""
os.unlink(path) = delete file at path 
os.rmdir(path) = deletes folder at path `
shutil.rmtree(path) = remove the folder at path 
"""
# os.unlink("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\move.txt")



#safe deletes
"""
safer to delete files using third party module : send2trash.
intall : pip install send2trash
it sends it to recyble bin instead of permanently deleting them.
"""
# import send2trash
# with open("safe_delete_file.txt","a") as file1:
#     file1.write("Testing dummy")
#
# send2trash.send2trash("safe_delete_file.txt")



# walking a directory tree
"""
os.walk() = you can look thorugh folder files, and folders of that folder , and do changes to each one 
"""
for folderName,subFolders,files in os.walk("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9"):
    print("current folder : "+folderName)

    for i in subFolders:
        print("Subfolder of : "+str(folderName)+":"+ str(subFolders))

    for i in files:
        print("Files are : "+str(folderName)+":"+str(files))

    print(" ")




#Compressing files with ZipFile Module
"""
we can create / extract zip files 
REading Zip files :
"""
import zipfile

# os.chdir("C:\\")
# exZip=zipfile.ZipFile("C:\\Users\\skyjd\Desktop\\test_zip_file.zip")
# print(exZip.namelist())
#
# info = exZip.getinfo("content.txt")  #looking at a txt file inside the zip file
# print(info.file_size)
#
# #compress said file now
# compress = info.compress_size
# print(compress)
#
# exZip.close()




#extracting from Zip file
"""
.extractall()
"""
# os.chdir("C:\\")
# exzip1 = zipfile.ZipFile("C:\\Users\\skyjd\Desktop\\test_zip_file.zip")
# exzip1.extractall("C:\\Users\\skyjd\\Desktop")
# exzip1.close()



#Creating and adding to zip files
"""
zipfile.ZIP_DEFLATED  = compression type parameter 
"""
new_zip_file = zipfile.ZipFile("C:\\Users\\skyjd\Desktop\\newzippy.zip","w")
new_zip_file.write("C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\organizing files chap 9\\04-11-1994.txt", compress_type=zipfile.ZIP_DEFLATED)
new_zip_file.close()


