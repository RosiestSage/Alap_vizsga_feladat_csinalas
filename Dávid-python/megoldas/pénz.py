import os
#1. feladat, váltás
os.system('cls')
reszveny = int(input("Adja meg mennyi részvényt venne: "))
print(f'\n{reszveny} db reszvény ára:')
print(f'\tOTP:  {18130 * reszveny} Ft')
print(f'\tMOL:  {3032 * reszveny} Ft')
print(f'\tBIF:  {564 * reszveny} Ft')
print(f'\tOpus:  {383.5 * reszveny:.0f} Ft')