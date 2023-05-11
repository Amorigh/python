# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:02:17 2022

@author: sch39270
"""


"""
def demo(**kwargs):
    print(kwargs)

demo(name="Humpty", location="wall")
"""
def mf(*kids):
    print("The youngest child is " + kids[-1])

mf("Emil", "Tobias", "Linus")

#################################################

def myf(**kid):
    print("His last name is " + kid["lname"])
    
myf(fname = "Tobias", lname = "Párek")

################################################
def dp(animal_type, pet_name):
    print("\nI have a " +animal_type+".")
    print("My " +animal_type+"'s name is " +pet_name.title()+".") #Title dává velké písmeno v pet_name
#1
dp("hamster", "harry")
#2
dp(animal_type="hamster", pet_name="harry")

################################################






