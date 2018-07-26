# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:12:32 2018

@author: kaan selim
"""
# this one's purpose is to find the lines without special characters or number
# and add them a special character

from string import punctuation
import time
special_char =list(punctuation)
print(len(special_char))
print(special_char)
in_file = open('out_file.txt', 'r+')
#out_file = open('out_file.txt', 'w')
#in_file = open('out_file.txt', 'r+')
out_file = open('out_file_new.txt', 'w')
# Read in the file
for line in in_file:

    print(line)
    if special_char[0] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[1] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[2] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[3] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[4] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[5] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[6] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[7] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[8] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[9] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[10] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[11] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[12] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[13] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[14] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[15] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[16] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[17] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[18] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[19] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[20] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[21] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[22] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[23] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[24] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[25] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[26] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[27] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[28] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[29] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[30] in line:
        print('found it !!!!!!!!!!!!!')
    elif special_char[31] in line:
        print('found it !!!!!!!!!!!!!')
    else:
        line = line+"!"
        print(line)
    out_file.write(line)

# Write the file out again

#out_file.write(line)



in_file.close()
out_file.close()
