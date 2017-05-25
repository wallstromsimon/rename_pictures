#!/usr/bin/python

import os

path = '/home/simonw/git/rename_pictures/pictures'
years = os.listdir(path)
years.sort()
i = 1

for year in years:
    yearPath = path + "/" + year
    folders = os.listdir(yearPath)
    folders.sort()
    yearCounter = 1
    print(year + ":")
    for folder in folders:
        folderPath = yearPath + "/" + folder
        pictures = os.listdir(folderPath)
        pictures.sort()
        camera = "OM"
        if "N0" in folder:
            camera = "N"
        print(folder + ":")
        for picture in pictures:
            picturePath = folderPath + "/" + picture
            if os.path.isfile(picturePath):
                newName = year + camera + '{0:04d}'.format(yearCounter) + ".JPG"
                print("    " + picture + " --> " + newName) 
                #os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
            yearCounter = yearCounter + 1

print("Steps: ", i)
