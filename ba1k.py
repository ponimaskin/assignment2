def FrequencyArray(text, k):
 array = []
 for i in range(0, 4**k):
  array.append(0) #der Wert für alle 4**k Möglichkeiten (in dem Fall 16) im array wird auf 0 gesetzt
 for i in range(0,len(text)-k+1):
  pattern=text[i:i+k]
  x=patternToNumber(pattern)
  array[x]=array[x]+1 #wird das pattern gefunden, so an der entsprechenden Stelle im array +1 
 return array

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
print(FrequencyArray('ACGCGGCTCTGAAA', 2))