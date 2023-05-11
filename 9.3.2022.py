# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:00:12 2022

@author: sch39270
"""
#1
jmena = "Pavel", "Radek", "Martin", "Petr", "Klara", "Simona", "Jakub"
print(jmena)


#2
osoba = {"jméno": "Jan","věk": 16, "hobby": "computer"}
print(osoba)
#3
glosar = {"variable -": "proměnná", "dictionary -": "slovník, je užit v tomto programu", "print -": "vytiskne to, co mu zadáte",
          "if -": "když je splněna nějaká podmínka vykoná se", "else -": "pokud něco nesedí pro if vykoná se else"}
for klic, hodnota in glosar.items():
     print(klic, hodnota)
#4     
zemereky = {"Vltava": "Czechia", "Yellow River": "China", "Amazon River": "Brazil"}
for klic, hodnota in zemereky.items():
    print(f"The {klic} runs trough {hodnota}.")
    
#5
telseznam = {"Nový": 789456123, "Modrá": 852456793, "Kindl": 123456789}
#a
telseznam["Horký"] =  559873145
print(telseznam)
#b
for klic, hodnota in telseznam.items():
    print(klic)
#c
a = int(input("Vyhledejte číslo podle jména:"))
if a == "Nový":
    print(hodnota)

     