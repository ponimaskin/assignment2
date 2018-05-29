def numberToPattern(x, k): #Symbol=x, Länge des Strings=k
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4) #// damit keine negativen Ergebnisse, % sodass jeweils der Restbetrag genommen wird

def numberToSymbol(x): #den Zahlen 0-3 wird ein Symbol zugeordnet
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

print(numberToPattern(45,4))