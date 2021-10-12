import re
from collections import Counter
from editdistancespellcheck import *

def makeSuggestions(text):
	text = text.lower()
	text = text.split(" ")
	newText = []
	for i in range(len(text)):
		if WORDS[text[i]] == 0:
			ans = known(oneEditDist(text[i]))
			newText.insert(i, ans[0])
		else:
			newText.insert(i, text[i])
	newText = " ".join(newText)
	return newText

print(makeSuggestions("This is a test sentecne"))




