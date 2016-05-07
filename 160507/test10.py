#!/usr/bin/env python 
#
num1=raw_input("Enter input num1") 
num2=raw_input("Enter input num2") 
num3=raw_input("Enter input num3") 

if int(num1)>int(num2) and int(num1)>int(num3):
    if int(num2)>int(num3):
      print num1+">"+num2+">"+num3
    else: 
      print num1+">"+num3+">"+num2
elif int(num2)>int(num1) and int(num2)>int(num3):
     if int(num1)>int(num3):
       print num2+">"+num1+">"+num3
     else: 
       print num2+">"+num3+">"+num1

elif int(num3)>int(num1) and int(num3)>int(num2):
     if int(num1)>int(num2):
       print num3+">"+num1+">"+num2
     else:
       print num3+">"+num2+">"+num1



