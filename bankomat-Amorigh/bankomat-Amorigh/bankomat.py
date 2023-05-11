def read_trezor(file):
    result = {}
    with open(file, "r") as f:
        while line := f.readline():
            bill, count = line.split()
            result[int(bill)] = int(count)
    return result


trezor = read_trezor("trezor.txt")

for bankovka, pocet in trezor.items():
    print(bankovka, pocet)


stav = 0

for bankovka, pocet in trezor.items():
    stav += bankovka * pocet
print(stav)

vyber = int(input("Kolik chceš vybrat?"))

cash = {}
soucet = vyber

if stav >= vyber:
    for bankovka, pocet in trezor.items():
        pocetbankovek = vyber//bankovka
        if pocetbankovek > 0 and pocet > 0:
            while pocetbankovek > 0 and pocet > 0:
                trezor[bankovka] -= 1
                vyber -= bankovka
                pocetbankovek -= 1
                pocet -= 1

                if (int(bankovka)) in cash:
                    cash[int(bankovka)] += 1
                else:
                    cash[int(bankovka)] = 1

    print(cash)
    print("bylo podáno: ")
    print(soucet)

else:

    print("Nedostatečný zůstatek")
