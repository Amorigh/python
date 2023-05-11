# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:53:28 2022

@author: sch39270
"""
import random
body = 0
kostka1 = [1,2,3,4,5,6]
kostka2 = [1,2,3,4,5,6]
kostka3 = [1,2,3,4,5,6]
kostka4 = [1,2,3,4,5,6]
kostka5 = [1,2,3,4,5,6]
kostka6 = [1,2,3,4,5,6]
vystup1 = random.choice(kostka1)
vystup2 = random.choice(kostka2)
vystup3 = random.choice(kostka3)
vystup4 = random.choice(kostka4)
vystup5 = random.choice(kostka5)
vystup6 = random.choice(kostka6)
vystupy = vystup1+vystup2+vystup3+vystup4+vystup5+vystup6
if vystup1 == 1:
    body = body + 100
if vystup1 == 5:
    body = body + 50

if vystup2 == 1:
    body = body + 100
if vystup2 == 5:
    body = body + 50

if vystup3 == 1:
    body = body + 100
if vystup3 == 5:
    body = body + 50

if vystup4 == 1:
    body = body + 100
if vystup4 == 5:
    body = body + 50

if vystup5 == 1:
    body = body + 100
if vystup5 == 5:
    body = body + 50

if vystup6 == 1:
    body = body + 100
if vystup6 == 5:
    body = body + 50
 
a =print(vystup1, vystup2, vystup3, vystup4, vystup5, vystup6)
print(f"máš {body} bodů")