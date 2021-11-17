import re
from collections import Counter
from ngram import *

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

#probability - divide how many times that word occurs by how many words total
def most_common(word, N=sum(WORDS.values())):
	return WORDS[word]/N

def ngram_prob(words):
	w = words[0]
	word = words[1]
	return (languagemodel(w,word)*error(word))

#we only want words that are real
def known(words):
	s = set(w for w in words if w in WORDS)
	x = list(s)
	return x

#possible replacements?
def possibleWords(word):
	return (known([word]) or known(oneEditDist(word)) or known(twoEditDist(word)) or [word])

#choose which one to be the actual correction
def correction(word):
	return max(possibleWords(word), key=most_common)

#create a list of all possible words that are one edit distance away
def oneEditDist(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return (deletes + transposes + replaces + inserts)

def twoEditDist(word):
    twoEdits = []
    for e1 in oneEditDist(word):
        for e2 in oneEditDist(e1):
            twoEdits.append(e2)
    return twoEdits
            
def getAllEdits(word):
	return oneEditDist(word)+twoEditDist(word)

