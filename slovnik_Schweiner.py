# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:08:00 2022

@author: sch39270
"""

seznam = {"key": "klic", "red": "červený", "dark": "tmavý", "bed": "postel", "fix": "spravit"}
while True:
    a = input("Zadejte slovo, které chcete přeložit:")
    if a == "stop":
        print("program ukončen")
        break
    print(seznam.get(a))