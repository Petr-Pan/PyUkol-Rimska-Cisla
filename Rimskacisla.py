romanize_dict = {0:'', 1:'I', 2:'II', 3:'III', 5:'V', 4:'IV',
				 6:'VI', 7:'VII', 8:'VIII', 
				 10:'X', 9:'IX', 20:'XX', 30:'XXX', 50:'L', 40:'XL', 60:'LX', 70:'LXX', 80:'LXXX',
				 100:'C', 90:'XC', 200:'CC', 300:'CCC', 500:'D', 400:'CD', 600:'DC', 700:'DCC', 800:'DCCC',
				 1000:'M', 900:'CM', 2000:'MM', 3000:'MMM',}

#Obrácení slovníku
unromanize_dict = {riman: arab for arab, riman in romanize_dict.items()}

def romanize(cislo):
	"""Zbaští číslo v desítkové soustavě a převede ho na římskou číslici. Horní hranice vstupního čísla je 3999. 
	Pro vyšší hodnotu nejsou v zadání znaky (Písmena s čárou nad nimi.)"""
	#Pro změnu vstupního čísla do seznamu a jeho následný rozklad v cyklu níže.
	#Z např. čísla '898' postupně vzniká seznam [800,90,8], jehož prvky jsou zároveň průběžně nahrazovány římskými číslicemi zprava.
	zlistovane_cislo = [int(znak) for znak in str(cislo)]
	transformator = 10 
	#Pomocné proměnné pro řízení cyklu
	i = 1
	delka = len(zlistovane_cislo)

	if delka > 1:
		while delka != i:
			zlistovane_cislo[-i] = romanize_dict.get(zlistovane_cislo[-i])
			zlistovane_cislo[-(i+1)] = zlistovane_cislo[-(i+1)] * transformator
			i += 1
			transformator *= 10
		zlistovane_cislo[-i] = romanize_dict.get(zlistovane_cislo[-i])
	else: 
		zlistovane_cislo[-i] = romanize_dict.get(zlistovane_cislo[-i])

	return ''.join(str(znak) for znak in zlistovane_cislo)

def unromanize(vstup):
	"""Převede římskou číslici na arabskou, v desítkové soustavě. Zcela omylem zvládá i nelegální zápisy (např. dobové XXXX)."""
	vystup = []

	for hodnota in reversed(list(unromanize_dict.keys())):
		if hodnota in vstup:
			vystup.append(unromanize_dict.get(hodnota))
			hotova_cast = len(hodnota)
			vstup = vstup[hotova_cast:]
			
	return sum(vystup)