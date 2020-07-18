from os import rename
from os import listdir
from os.path import isfile, join

folder = input('Enter folder name (Unix style) :')
files = [f for f in listdir(folder) if isfile(join(folder, f))]
phrase = input("Enter the phrase you wish to delete :")

count = 0
for i in files:
    idx = i.find(phrase)
    if(idx == -1):
        print("Can't Rename")
    else:
        new_name = i[ :idx] +'.mp4'
        rename(join(folder, i), join(folder, new_name))
        count += 1
        print("Rename Done !")
        
print("Rename done for {} files.".format(count))