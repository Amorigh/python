# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:30:06 2022

@author: sch39270
"""

def funkce1():
    x=10 #lokální proměnná
    print(x) #tisk lokální proměnné
funkce1()

#######################

z=1 #globální proměnná
def funkce2():
    z=10 #lokální proměnná
    print(z) #tisk lokální proměnné
funkce2()

#########################

y=1 #globální proměnná
def funkce3():
    global y #použití globální proměnné
    print(y) #tisk globální proměnné
funkce3()
print(y) #tisk globální proměnné