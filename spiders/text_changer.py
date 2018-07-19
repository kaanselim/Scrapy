# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:12:32 2018

@author: kaan selim
"""

in_file = open('dosya.txt', 'r+') 
out_file = open('out_file.txt', 'w')

# Read in the file

filedata = in_file.read()


filedata = filedata.replace('a', '@')

filedata = filedata.replace('i','1')
filedata = filedata.replace('A','4')
filedata = filedata.replace('b','6')
filedata = filedata.replace(' ','_')
filedata = filedata.replace('E','3')

# Write the file out again
out_file.write(filedata)



in_file.close()
out_file.close()