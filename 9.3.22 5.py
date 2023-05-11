# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:06:30 2022

@author: sch39270
"""

telseznam = {"Nový": 789456123, "Modrá": 852456793, "Kindl": 123456789}

print("Co potřebujete? \n1)přidat záznam \n2)výpis jmen \n3)vyhledat číslo podle jména \n4)výpis čísel ")
while True:
    volba = int(input("Vaše volba:"))
    if volba == 1:
        jm = input("Zadejte jméno:")
        cs = input("Zadejte číslo:")
        telseznam[jm] = cs
    if volba == 2:
        for klic, hodnota in telseznam.items():
            print(klic)
    if volba == 3:
        a = str(input("Vyhledejte číslo podle jména:"))
    
        if a == "Nový":
            print(telseznam.get(a))
        elif a == "Modrá":
            print(telseznam.get(a))
        elif a == "Kindl":
            print(telseznam.get(a))
        elif a == "Horký":
            print(telseznam.get(a))
    if volba == 4:
        for klic, hodnota in telseznam.items():
            print(hodnota)
    
