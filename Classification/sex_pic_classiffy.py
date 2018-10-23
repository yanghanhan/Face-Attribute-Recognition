# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:37:03 2018

@author: Administrator
"""

import os
import shutil

nof = open("notMale.txt")
hasf = open("Male.txt")

noLine = nof.readline() 
hasLine = hasf.readline() 

list = os.listdir("E:/bigdata/CelebA/Img/img_align_celeba")
hasGo = True
noGo = True
print(len(list))
for i in range(0, len(list)):
    imgName = os.path.basename(list[i])
    if (os.path.splitext(imgName)[1] != ".jpg"): continue

    noArray = noLine.split()
    if (len(noArray) < 1): noGo = False
    hasArray = hasLine.split()
    if (len(hasArray) < 1): hasGo = False

    if (noGo and (imgName == noArray[0])):
        oldname= "E:/bigdata/CelebA/Img/img_align_celeba/"+imgName
        newname="E:/bigdata/CelebA/Img/notMale/"+imgName
        shutil.copy(oldname, newname)
        noLine = nof.readline()
    elif (hasGo and (imgName == hasArray[0])):
        oldname= "E:/bigdata/CelebA/Img/img_align_celeba/"+imgName
        newname="E:/bigdata/CelebA/Img/isMale/"+imgName
        shutil.copy(oldname, newname)
        hasLine = hasf.readline()

    if (i % 100 == 0): print(imgName)

nof.close()
hasf.close()
