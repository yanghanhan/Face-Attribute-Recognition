# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:55:34 2018

@author: Administrator
"""

f = open("E:/bigdata/CelebA/Anno/list_attr_celeba.txt")
newTxt = "Male.txt"
newf = open(newTxt, "a+")
newNoTxt = "notMale.txt"
newNof = open(newNoTxt, "a+")

line = f.readline() 
line = f.readline() 
line = f.readline() 
while line:
    array = line.split()
    if (array[0] == "000007.jpg"): print(array[21])

    if (array[21] == "-1"): 
        new_context = array[0] + '\n'
        newNof.write(new_context)
    else: 
        new_context = array[0] + '\n'
        newf.write(new_context)
    line = f.readline()

lines = len(newf.readlines()) 
print ("There are %d lines in %s" % (lines, newTxt)) 
lines = len(newNof.readlines()) 
print ("There are %d lines in %s" % (lines, newNoTxt))

f.close()
newf.close()
newNof.close()