# -*- coding: utf-8 -*-

"""
import random 
colors = ["Red", "Black", "Green"]
results = random.choices(colors, weights=[18,18,2], k=10)
print(results)
"""
"""
import random
#for i in range(20):
#    print(random.normalvariate(0, 1))
for i in range(20):
    print(random.normalvariate(0, 9))
#for i in range(20):
#    print(random.normalvariate(5, 0.2))
"""
"""
import random 
hodnoty = list(range(1,53))

random.shuffle(hodnoty)
print(hodnoty)
"""
"""
import random
hodnoty = list(range(1,53))

vyber = random.sample(hodnoty,k=5)
print(vyber)
"""
import random
hodnoty = list(range(1,11))
spravne = random.choice(hodnoty)
pokusy = int(input("Kolik chcete pokusů?: "))

for i in range(pokusy):
    hadani = int(input("Zkuste uhodnout číslo v řadě 1 až 10: "))
    
    if spravne == hadani:
        print("Správně")
        break
    elif spravne > hadani:
        print("Špatně, číslo je větší")
        pokusy = pokusy - 1
    elif spravne < hadani:
        print("Špatně, číslo je menší")
        pokusy = pokusy - 1

print(f"Číslo bylo {spravne}")


