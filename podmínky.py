"""
1)
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
if a>b:
    print("první číslo je větší")
elif a<b:
    print("druhé číslo je větší")
elif a==b:
    print("čísla jsou stejná")

2)
a = int(input("Zadej číslo a já ti řeknu, zda-li je sudé nebo liché: "))
b = a%2
if b==0:
    print("číslo je sudé")
else:
    print("číslo je liché")

3)
heslo = input("Zadej heslo: ")
if heslo in "lachtan":
    print("správné heslo")
else:
    print("špatné heslo")
"""    