# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:10:49 2022

@author: sch39270
"""

SK={}
SK["vrtacka"]=["vrtacka","Neorex","naradi"]
SK["sada nozu"]=["sada nozu","KSL","kuchyn"]
SK["meric"]=["meric","Zmat","pristroje"]
SK["slehac"]=["slehac","Solomat","kuchyn"]
SK["svarecka"]=["svarecka","Neorex","naradi"]

#a
for klic, hodnota in SK.items():
    print(f"{klic} = {hodnota}")

#b
vypis1 = input("Podle seznamu výše si zvolte jednu položku k výpisu: ")
print(SK.get(vypis1))

#c
print("Přidáváte novou položku")
for i in range(2):
    vec = input("Napište název položky: ")
    typ = input("Napište typ položky: ")
    znacka = input("Napište značku položky: ")
    misto = input("Napište umístění položky: ")
    SK[vec] = typ, znacka, misto
    for klic, hodnota in SK.items():
        print(f"{klic} = {hodnota}")

#d
print("Přidejte vlastnost na konec každého záznamu: ")
novahodnota = input("")
for klic, hodnota in SK.items():
    SK[klic] = [hodnota] + [novahodnota]
for klic, hodnota in SK.items():
    print(f"{klic} = {hodnota}")