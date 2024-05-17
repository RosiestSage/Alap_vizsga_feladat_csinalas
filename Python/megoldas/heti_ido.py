list = ['Hétfőn', 'Kedden', 'Szerdán', 'Csütörtökön', 'Pénteken', 'Szombaton', 'Vasárnapon']
osszperc = 0

def percek(ora, perc):
    return int(ora) * 60 + int(perc)

for i in range(0, 7):
    ora = input(f"{list[i]} eltöltött óra: ")
    perc = input(f"{list[i]} eltöltött perc: ")
    print()
    osszperc += percek(ora, perc)


print(f"A héten összesen {osszperc} percet töltöttél edzéssel")



