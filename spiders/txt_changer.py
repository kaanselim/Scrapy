# -*- coding: utf-8 -*-


# This code is used to remove any lines that has only white blanks




infile = open('dosya.txt', 'r+')

new_file = infile.read()

infile.seek(0)

thing_to_write = "".join([s for s in new_file.strip().splitlines(True) if s.strip("\r\n").strip()])
infile.write(thing_to_write)

infile.truncate()

#for line in new_file: ---------- in this part i deleted the lines with integers that i dont want 
 #   if "5" not in line:
  #      infile.write(line)
  
  
infile.close()