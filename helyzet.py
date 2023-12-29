

from GepClass import Gep



def fajlBeolvas():
	fajl = open("gep.txt","r",encoding="UTF-8")
	fajl.readline()
	sorokLista = fajl.readlines()
	fajl.close()

	gepLista = []
	for i in range(0,len(sorokLista),1):
		aktElem = sorokLista[i]
		sorLista = aktElem.strip().split("!")
		idd = int(sorLista[0])
		hely = str(sorLista[1])
		tipus = str(sorLista[2])
		ipcim = sorLista[3]

		gep = Gep(idd,hely,tipus,ipcim)
		gepLista.append(gep)

	return gepLista






def GepekSzama():
	lista = fajlBeolvas()
	db = 0
	for gep in lista:
		db += 1
	return db





def AzonositoAtlag():
	lista = fajlBeolvas()
	szamlalo, osszeg = 0, 0
	for i in range(0,len(lista),1):
		if int(lista[i].hely[-1]) % 2 == 0:
			osszeg += lista[i].idd
			szamlalo += 1
	return round(osszeg / szamlalo, 2)





def LegkisebbAzonosito():
	lista = fajlBeolvas()
	legkis, adatok = 500, 0
	for i in range(0,len(lista),1):
		if lista[i].tipus == "asztali":
			if lista[i].idd < legkis:
				legkis = lista[i].idd
				adatok = lista[i].idd, lista[i].hely 
	return adatok

















