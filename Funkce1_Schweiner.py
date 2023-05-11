# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:01:48 2022

@author: sch39270
"""

def urceni(cislo1, cislo2, cislo3):
    if cislo1 > cislo2 and cislo3:
        print("ono číslo je" ,cislo1)
    elif cislo2 > cislo1 and cislo3:
        print("ono číslo je" ,cislo2)
    elif cislo3 > cislo1 and cislo2:
        print("ono číslo je" ,cislo3)

cislo1 = int(input("číslo 1: "))
cislo2 = int(input("číslo 2: "))
cislo3 = int(input("číslo 3: "))
urceni(cislo1, cislo2, cislo3)