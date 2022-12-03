import random
'''
Projekt neve: Sajat_nev_gyakorlas

1. Készíts egy sorozat nevű tömböt a következő elemekkel: -3, 5, 11, -2, 4
2. Készíts egy metódust, ami kiírja a tömb elemeit egymás mellé, a metódus paraméterében kapott szeparátor felhasználásával!
   Az utolsó elem után ne legyen szeparátor!
   pl: separator: "# " -3# 5# 11# -2# 4
3. Változtasd meg a tömb elemeit a következő módon:
3/1. A tömb első eleméhez adj egy véletlenszámot a [5; 12] intervallumból!
3/2. Az utolsó elem értékét kérd be, ez páratlan hárommal osztható kéjegyű szám legyen! Ha nem ilyen számot adnak meg,
     akkor addig folytassa a program a bekérést, amíg megfelelő nem lesz a bekért szám! A bekéréshez készíts külön függvényt!
3/3. Használd a 2. feladat kiíró metódusát paraméter nélkül, ekkor szóközzel írja ki a tömb elemeit, egymás mellé!
3/4. Add meg az első kétjegyű szám helyét és  értékét a tömbből!
3/5. Számold meg, hogy hány prímszám van a tömbben! Ehhez készíts külön függvényt, ami eldönti, hogy a paraméterében kapott szám prímszám-e?
'''

# 2. Készíts egy metódust, ami kiírja a tömb elemeit egymás mellé,
#    a metódus paraméterében kapott szeparátor felhasználásával!
#    Az utolsó elem után ne legyen szeparátor!
#    pl: separator: "# " -3# 5# 11# -2# 4
def kiir(lista, elvalaszto=" "):
    if not lista:
        return
    szoveg = str(lista[0])
    i = 1
    while i < len(lista):
        szoveg += elvalaszto + str(lista[i])
        i += 1
    print(szoveg)

# 3. Változtasd meg a tömb elemeit a következő módon:
# 3/1. A tömb első eleméhez adj egy véletlenszámot a [5; 12] intervallumból!
def hozzaad_veletlent(lista):
    # ha van elem a listán
    if len(lista):
        lista[0] += int(random.random() * 8) + 5
    else:
        print("Nem lehet a tömb első elemét módosítani, a tömb üres.")


# 3/2. Az utolsó elem értékét kérd be, ez páratlan hárommal osztható kéjegyű szám legyen!
# Ha nem ilyen számot adnak meg, akkor addig folytassa a program a bekérést,
# amíg megfelelő nem lesz a bekért szám! A bekéréshez készíts külön függvényt!
def paratlan_oszthato(lista):
    szam = 0
    while szam > 100 or szam < 10 or szam % 3 != 0 or szam % 2 == 0:
        # szam = int(input("Adjon meg egy hárommal osztható, kétjegyű, páratlan számot! "))
        szam = 99
    lista.append(szam)

# 3/3. Használd a 2. feladat kiíró metódusát paraméter nélkül, ekkor szóközzel írja ki a tömb elemeit, egymás mellé!
# Megjegyzes: csak azért csináltam rá függvényt, minden feladathoz tartozó hívás ebben a modulban legyen.
def kiir_param_nelkul(lista):
    kiir(lista)

# 3/4. Add meg az első kétjegyű szám helyét és  értékét a tömbből!
def elso_ketjegyu_a_listan(lista):
    idx = 0
    i = 0
    while i < len(lista) and abs(lista[i]) < 10 or abs(lista[i]) >= 100:
        i += 1
    if i < len(lista):
        print(f"Első kétjegyű szám: {lista[i]} indexe: {i}")
    else:
        print("Nincs kétjegyű szám a listán")


# 3/5. Számold meg, hogy hány prímszám van a tömbben!
# Ehhez készíts külön függvényt, ami eldönti, hogy a paraméterében kapott szám prímszám-e?
def prim_e(num):
    # ha a szám kisebb, vagy egyenlő 1, nem lehet prímszám
    if num <= 1:
        return False

    vizsgalat_vege = num ** (1 / 2)

    # ha a szám gyöke egész szám, akkor az négyzetszám, tehát nem prímszám
    if vizsgalat_vege == int(vizsgalat_vege):
        return False

    # ha kettővel osztható, nem prímszám
    if num % 2 == 0:
        return False

    # háromtól kezdünk, a szám gyökéig.
    # amint osztót találunk, visszatérünk hamissal.
    # mivel páros csak páros számok jöhetnek szóba, kettesével lépkedünk
    i = 3
    while i <= int(vizsgalat_vege):
        if num % i == 0:
            return False
        i += 2

    return True

def primeket_szamol(lista):
    db = 0
    i = 0
    while i < len(lista):
        if prim_e(lista[i]):
            db += 1
        i += 1
    if not db:
        print("Nincs prímszám a listán")
    else:
        print(f"{db} prímszám van a listán")

