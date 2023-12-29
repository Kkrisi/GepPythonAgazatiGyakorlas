

import minosites
import sorozat
import helyzet




# Feladat 1.
adat = minosites.Adatok()

print(f"I/A:\n\n\tMúzeum neve: {adat[0]}\n\n\tLátogató neve: {adat[1]}\n\n\tÉrtékelés (1-20): {adat[2]}")
print(f"\nI/B:\n\n\t{adat[3]}")






# Feladat 2.
lista = sorozat.Szamsor()

sorozat.oszthatoak_szama(lista)

sorozat.konzolra_kiir()

sorozat.fajl_ir()








# Feladat 3.
gepek = helyzet.GepekSzama()
print(f"III/A, B:\n\n\tA gépek száma: {gepek}.")


atlag = helyzet.AzonositoAtlag()
print(f"\nIII/C:\n\n\tA páros teremszámú termek azonosító átlaga: {atlag}")


adatok = helyzet.LegkisebbAzonosito()
print(f"\nIII/D:\n\n\tA legkisebb asztali gép azonosítója: {adatok[0]}, helye: {adatok[1]}")



















