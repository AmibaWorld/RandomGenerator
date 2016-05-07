#!/usr/bin/env python
#
import os
ls =os.linesep

print "write file--1"
print "read  file--2"
num=raw_input("Enter input chooise")
print num
if num=="1" :
     
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

elif num=="2":

     fname=raw_input('Enter filename:')
     try:
       fobj=open(fname,'r')
     except IOError,e:
       print "no file , i am sorry "
     else:
       for eachLine in fobj:
          print eachLine
       fobj.close()  

else : 
    print "you choice error"
 	
