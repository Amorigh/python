# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:16:40 2022

@author: sch39270
"""

import random
kola = int(input("Kolik chcete kol?"))
hrac = 0
pcv = 0
vyhry = 0



for x in range(kola):
    hrac = input("Kámen(K), Nůžky(N), Papír(P)?")
    pcv = random.randint(1,3)
    if hrac == "K" and pcv == 1:
        vyhry = vyhry + 1
        print("vyhrál jsi kolo")
        
    elif hrac == "N" and pcv == 2:
        vyhry = vyhry + 1
        print("vyhrál jsi kolo")
        
    elif hrac == "P" and pcv == 3:
        vyhry = vyhry + 1
        print("vyhrál jsi kolo")
        
    elif hrac == "K" and pcv == 2:
        vyhry = vyhry + 0
        print("nerozhodně")
        
    elif hrac == "K" and pcv == 3:
        vyhry = vyhry + 0
        print("prohrál jsi kolo")
        
    elif hrac == "N" and pcv == 1:
        vyhry = vyhry + 0
        print("nerozhodně")
        
    elif hrac == "N" and pcv == 3:
        vyhry = vyhry + 0
        print("prohrál jsi kolo")
        
    elif hrac == "P" and pcv == 1:
        vyhry = vyhry + 0
        print("nerozhodně")
        
    elif hrac == "P" and pcv == 2:
        vyhry = vyhry + 0
        print("prohrál jsi kolo")
        
print(f"Vyhrál jsi: {vyhry}krát")
    
        