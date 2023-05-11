# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:58:19 2022

@author: sch39270
"""
import math
nakolik = 0
cislo = int(input("Jaké číslo chcete umocnit?"))
nakolik = int(input("Na kolikátou?"))
def mocnina(cislo, nakolik):
    
    mocnina = math.pow(cislo, nakolik)
    if nakolik == 0:
        nakolik = 2
    print(mocnina)
mocnina(cislo, nakolik)
"nedokázal jsem vymyslet druhou mocninu při prázdném inputu"