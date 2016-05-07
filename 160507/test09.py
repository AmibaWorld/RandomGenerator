#!/usr/bin/env python 

ss=[1,2,3,4,5]
i =0
while i <2: 
  print "(1) please get five sum"
  print "(2) please get five avg"
  print "(3) exit"
  num=raw_input("Enter input num") 
  if int(num)==1 :
     print sum(ss) 
  elif int(num)==2 : 
     print sum(ss)/len(ss)
  else : 

       break
