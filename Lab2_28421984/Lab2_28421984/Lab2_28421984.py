def validWord(word:str)->bool:
	valid = True
	word = word.lower()
	i = 0
	while i < len(word):
		if (word[i] != "a" and word[i] != "e" and word[i] != "i" and word[i] != "o" 
		and word[i] != "u" and word[i] != "p" and word[i] != "k" and word[i] != "h" 
		and word[i] != "l" and word[i] != "m" and word[i] != "n" and word[i] != "w" 
		and word[i] != "'" and word[i] != " "):
			valid = False
		i = i + 1
	return valid

def pronunciate(phrase:str)->str:
	phrase = phrase.lower()
	words = phrase.split()
	newStr = ""

	for i in words:
		newStr = newStr + " " + proHelp(i)

	newStr = newStr.strip()
	return newStr

def proHelp(phrase:str)->str:
	newStr = ""
	i = 0
	while i < len(phrase):
		if phrase[i] == "'":
			newStr = newStr.rstrip('-')
			newStr = newStr + "'"
		else:
			if (phrase[i] == "p" or phrase[i] == "k" or phrase[i] == "h" or phrase[i] == "l" 
			or phrase[i] == "m" or phrase[i] == "n"):
				newStr = newStr + phrase[i]
			elif phrase[i] == "w":
				newStr = newStr + w(phrase, i)
			else:
				letter = ""
				if phrase[i] == "a":
					if i == len(phrase)-1:
						letter = "ah"
					elif phrase[i+1] == "i" or phrase[i+1] == "e":
						letter = "eye"
						i = i + 1
					elif phrase[i+1] == "o" or phrase[i+1] == "u":
						letter = "ow"
						i = i + 1
					else:
						letter = "ah"
				elif phrase[i] == "e":
					if i == len(phrase)-1:
						letter = "eh"
					elif phrase[i+1] == "i":
						letter = "ay"
						i = i + 1
					elif phrase[i+1] == "u":
						letter = "eh-oo"
						i = i + 1
					else:
						letter = "eh"
				elif phrase[i] == "i":
					if i == len(phrase)-1:
						letter = "ee"
					elif phrase[i+1] == "u":
						letter = "ew"
						i = i + 1
					else:
						letter = "ee"
				elif phrase[i] == "o":
					if i == len(phrase)-1:
						letter = "oh"
					elif phrase[i+1] == "i":
						letter = "oy"
						i = i + 1
					elif phrase[i+1] == "u":
						letter = "ow"
						i = i + 1
					else:
						letter = "oh"
				elif phrase[i] == "u":
					if i == len(phrase)-1:
						letter = "oo"
					elif phrase[i+1] == "i":
						letter = "ooey"
						i = i + 1
					else:
						letter = "oo"
				newStr = newStr + letter + "-"
		i = i + 1

	newStr = newStr.rstrip('-')
	newStr = newStr.capitalize()
	return newStr

def w(phrase:str, loc:int)->str:
	letter = "w"
	if loc == 0 or phrase[loc-1] == "a" or phrase[loc-1] == "u" or phrase[loc-1] == "o":
		letter = "w"
	elif phrase[loc-1] == "i" or phrase[loc-1] == "e":
		letter = "v"
	return letter

def validWordFile(word:str)->bool:
	valid = True
	word = word.lower()
	i = 0
	while i < len(word):
		if (word[i] != "a" and word[i] != "e" and word[i] != "i" and word[i] != "o" 
		and word[i] != "u" and word[i] != "p" and word[i] != "k" and word[i] != "h" 
		and word[i] != "l" and word[i] != "m" and word[i] != "n" and word[i] != "w" 
		and word[i] != "'" and word[i] != " " and word[i] != "," and word[i] != "."):
			valid = False
		i = i + 1
	return valid

def createGuide(inputFile:str, outputFile:str):
	try:
		infile = open(inputFile, "r")
	except IOError:
		print("Error: file not found.")
		return
	try:
		outfile = open(outputFile, "w")
		try:
			line = infile.readline()
			while line != "":
				newStr = ""
				line = line.strip("\n")
				strList = line.split()

				for i in strList:
					valid = validWordFile(i)
					if valid == True:
						k = (len(i) - 1)
						if i[k] == ".":
							newStr = newStr + pronunciate(i[:k]) + ". "
						elif i[k] == ",":
							newStr = newStr + pronunciate(i[:k]) + ", "
						else:
							newStr = newStr + pronunciate(i) + " "
					else:
						newStr = newStr + '"' + i + '" '
		
				newStr = newStr.strip()
				line = infile.readline()
				if line != "":
					outfile.write(newStr+"\n")
				else:
					outfile.write(newStr)
		finally:
			outfile.close()
	except IOerror:
		print("Error: IO error.")
		return

	infile.close()
	return