# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:16:42 2022

@author: sch39270
"""

import random
cisla = list(range(1,21))
vyber = random.choices(cisla, weights=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(f"nejmenší číslo je {vyber}")
print(f"jeho pořadí je {vyber}")
