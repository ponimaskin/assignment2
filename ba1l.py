def patternToNumber(pattern):
	if len(pattern) == 0: #alle Möglichkeiten definieren, auch wenn kein Input gegeben
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:]) #4 verschiedene Symbole, string wird von hinten gelesen
             #bis zur vorletzen Stelle des strings   #das letzte Symbol des strings
def symbolToNumber(symbol): #Jedem möglichen Symbol wird eine Zahl zugeordnet
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

print(patternToNumber("CTTCTCACGTACAACAAAATC")) #Ausführen der Funktion