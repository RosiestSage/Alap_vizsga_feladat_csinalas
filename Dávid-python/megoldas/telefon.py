class Telefonszam:
    def __init__(self, nev, telefonszam, munka):
        self.nev = nev
        self.telefonszam = telefonszam
        self.munka = munka

telefonszamok: list[Telefonszam] = []

for i in range(5):
    nev = input('Név: ')
    telefonszam = input("Telefonszám: +36 ")
    munka = input("Céges/Magán: ")
    telefonszamok.append(Telefonszam(nev, telefonszam, munka))
    print()

for i in range(len(telefonszamok)):
    print(f"{telefonszamok[i].nev} telefonszáma: +36 {telefonszamok[i].telefonszam} ami {telefonszamok[i].munka}")

f = open("cegesek.txt", "w", encoding="utf-8")
for t in telefonszamok:
    if t.munka == "Céges":
        f.write(f"{t.nev}; +36 {t.telefonszam};{t.munka}")
f.close()

f = open("magánok.txt", "w", encoding="utf-8")
for t in telefonszamok:
    if t.munka == "Magán":
        f.write(f"{t.nev}; +36 {t.telefonszam};{t.munka}")
f.close()