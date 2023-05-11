# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:51:42 2022

@author: sch39270
"""

vklad = int(input("číslo:"))
if vklad % 3==0:
    print("fizz")
if vklad % 5==0:
    print("buzz")
if vklad % 3 and 5==0:
    print("Fizzbuzz")
else:
    print(vklad)