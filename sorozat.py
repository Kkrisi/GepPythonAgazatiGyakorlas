

import random


def Szamsor():
	global lista
	lista = []
	for i in range(15):
		szam = random.randint(-90,500)
		lista.append(szam)

	print(f"\nII/A, B, C:\n\t")
	szamlalo = 0
	for eredmeny in lista:
		szamlalo += 1
		if szamlalo == len(lista):
			print(eredmeny,end="")
		else:
			if szamlalo == 1:
				print("\t",eredmeny,end="*")
			else:
				print(eredmeny,end="*")
	return lista





def oszthatoak_szama(lista):
	szamlalo = 0
	for szam in lista:
		if szam % 10 == 0:
			szamlalo += 1
	return round(szamlalo)
		




def konzolra_kiir():
	szam = oszthatoak_szama(lista)
	print(f"\n\nII/D, E:\n\n\tTízzel osztható számok száma: {szam}.")

	




def fajl_ir():
	szam = oszthatoak_szama(lista)
	f = open('kimutatas.txt','w')
	f.write(f"II/F:\n\tTízzel osztható számok száma: {szam}.")
	f.close()




































