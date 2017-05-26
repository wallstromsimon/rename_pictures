#!/usr/bin/python

import os

path = '/home/simonw/Pictures/digitala/Nikon'
years = os.listdir(path)
years.sort()

# For every year
for year in years:
    yearPath = path + "/" + year
    folders = os.listdir(yearPath)
    folders.sort()
    yearCounter = 1
    print(year + ":")
    # For every subfolder
    for folder in folders:
        folderPath = yearPath + "/" + folder
        pictures = os.listdir(folderPath)
        pictures.sort()
        camera = "OM"
        if "N0" in folder:
            camera = "N"
        print(folder + ":")
        # For every picture
        for picture in pictures:
            picturePath = folderPath + "/" + picture
            if os.path.isfile(picturePath) and "Thumbs" not in picture:
                newName = year + camera + '{0:04d}'.format(yearCounter) + ".JPG"
                print("    " + picture + " --> " + newName) 
                os.rename(picturePath, folderPath + "/" + newName)
                yearCounter = yearCounter + 1

