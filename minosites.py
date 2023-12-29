



def Adatok():
	muzeum = str(input("Add meg a múzeum nevét: "))
	latogato = str(input("Add meg a látogató nevét: "))
	ertekeles = int(input("Add meg az értékelést: "))
	if ertekeles == 0:
		valasz = "Az értékelés nem lehet negatív vagy 0!"
	elif ertekeles > 20:
		valasz = "20 pont feletti értékelés nem elfogadható!"
	else:
		valasz = "Köszönjük az értékelést!"
	return muzeum, latogato, ertekeles, valasz
































