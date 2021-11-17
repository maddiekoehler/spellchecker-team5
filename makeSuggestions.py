import re
from collections import Counter
from editdistancespellcheck import *
from ngram import *

#Baysean implementation of generating replacement words, sorted by frequency in a file
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

#generate replacements based on context (probability defined as language model * error model)
def newSuggest(text):
	text = text.lower()
	mytup = splitSentence(text)
	problist = []
	choices = possibleWords(mytup[1])
	for choice in choices:
		temptup = (mytup[0], choice)
		n = ngram_prob(temptup)
		problist.append((choice,n))
	problist.sort(key=lambda a: a[1], reverse=True)
	optionlist = []
	for tup in problist:
		optionlist.append(tup[0])
	return optionlist

def pickOne(text):
	choices = newSuggest(text)
	return choices[0]

	
#identify words that are misspelled
def getMisspelled(words):
	wrong=[]
	words = words.lower()
	words = words.split(" ")
	for word in words:
		if word not in known(words):
			wrong.append(word)
	return wrong

#split input string into tuple of context and misspelled word
def splitSentence(text):
	wrongWords = getMisspelled(text)
	text = text.split(' ')
	tuplist = []
	for w in wrongWords:
		for i in range(len(text)):
			if w == text[i]:
				lastTwo = " ".join(text[i-2:i])
				target = text[i]
				#tuplist.append((lastTwo, target))
	#return tuplist
	return(lastTwo, target)

#print(splitSentence('this is a test sentecne'))
#print(getMisspelled('this is a test sentecne'))
#print(makeSuggestions('this is a test sentecne'))
#print(ngram_prob(splitSentence('this is a test sentecne')))
#print(languagemodel(splitSentence('this is a test sentence')[0]))
#print(newSuggest('a big mna'))
#print(splitSentence('this is wrnog and so is tihs'))
#print(newSuggest('this is wrnog and so is tihs'))
#print(pickOne('this is wrnog and so is tihs'))
