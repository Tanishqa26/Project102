import os
import shutil
from_dir = "C:/Users/Anushka/Documents/class c102/images"
to_dir = "C:/Users/Anushka/Documents/python/Document_files"
list_of_files= os.listdir(from_dir)
print(list_of_files)

for Flowers_jpg  in list_of_files:

    name,extension = os.path.splitext(Flowers_jpg)
    print(name)
    print(extension)

    if extension=='':
        continue

    if extension in ['.txt', '.doc', '.docx', '.pdf']:
         path1= from_dir +'/'+ Flowers_jpg
         path2 = to_dir + '/' + "Document_Files"
         path3 = to_dir + '/' + "Document_Files" + Flowers_jpg

         #Check if the Folder/Directory Exists before Moving
         #Else make a NEW Folder/Directory then move

         if os.path.exists(path2):
             print("Moving " + Flowers_jpg + '.....')

             #Move from path1 ---> path3
             shutil.move(path1,path3)

         else:
             os.makedirs(path2)
             print("Moving " + Flowers_jpg + '.....')
             shutil.move(path1,path3)






    
 


