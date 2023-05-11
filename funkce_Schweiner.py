# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:54:11 2022

@author: sch39270
"""
pozdrav = input("Jaký je pozdrav?")
kolik = int(input("Kolikrát se má opakovat?"))
def SP(pozdrav, kolik):
    for pocet in range(kolik):
        print(pozdrav)
SP(pozdrav, kolik)