# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:52:11 2022

@author: sch39270
"""

veta = input("Zadejte větu:")

#1
print("Počet znaků: " + str(veta.count("")))
#2
if "x" in veta:
    print('Písmeno x je ve větě a to ' + str(veta.count("x",)))
else:
    print('Písmeno x není ve větě')

if "x" in veta:
    print('Písmeno y je ve větě a to ' + str(veta.count("y")))
else:
    print('Písmeno y není ve větě')
#3
print(veta.upper())
#4
posledni1 = ""
posledni2 = ""
posledni3 = ""
posledni4 = ""
posledni5 = ""

for i in range(1):
    posledni1 += veta[-1]
posledni2 = ""

for i in range(1):
    posledni2 += veta[-2]
posledni3 = ""

for i in range(1):
    posledni3 += veta[-3]
posledni4 = ""

for i in range(1):
    posledni4 += veta[-4]
posledni5 = ""

for i in range(1):
    posledni5 += veta[-5]

print(posledni1, posledni2, posledni3, posledni4, posledni5)
