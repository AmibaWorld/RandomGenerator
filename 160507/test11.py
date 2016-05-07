#!/usr/bin/env python 
#
import os
ls =os.linesep

fname=raw_input("Enter input file:");
while True:
   if os.path.exists(fname):
 	print "ERRORL: '%s' already exists" % fname
   else:
        break

all=[]
print "\nEnter lines ('.' by itself to quit).\n"

while True:
  entry=raw_input("input want font >>")
  if entry=='.':
     break
  else:
      all.append(entry)
fobj=open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print "DONE"
