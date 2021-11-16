import re
from collections import Counter
from editdistancespellcheck import *

def makeSuggestions(text):
	text = text.lower()
	text = text.split(" ")
	newText = []
	for i in range(len(text)):
		if text[i] not in known(text):
			newText.append(sorted(possibleWords(text[i]), key=most_common, reverse=True))
			return newText
		else:
			return text[i]



def getMisspelled(words):
	wrong=[]
	words = words.lower()
	words = words.split(" ")
	for word in words:
		if word not in known(words):
			wrong.append(word)
	return wrong
			
