import os
import datetime
import re

print("\nVideo Recordings Rename-Script\n")
folder = os.path.abspath(input('Enter folder path :'))
files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
info = dict()
number = 1

phrase = input("Enter the phrase you wish to delete :")
extension = input("Enter the File Extension (example - .mp4) :")
number = int(input("From where you wish to start the numbering ? (Enter an integer) :"))

files = [file for file in files if(file[-4:] == extension)]

for file in files:
    timestamp = os.path.getmtime(os.path.join(folder, file))
    if(info.get(file) is None):
        date = datetime.datetime.fromtimestamp(timestamp)
        info[file] = [str(date)]

data = dict(sorted(list(info.items()),key = lambda x : x[1]))
for i,file in enumerate(data):
    result = re.search(r"[a-zA-Z][\w\s\-\&,]*[\.]", file)
    new_name = "{}. {}".format(i + number, result[0]) + extension
    idx = new_name.find(phrase)
    if(idx != -1):
        new_name = new_name[ :idx] + extension
    os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
    print("Rename Done !")
