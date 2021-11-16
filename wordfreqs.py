import random, re, codecs, sys
import pickle

def singleWordFrequency(txt):#wordfrequency.py
	string = open('big.txt').read().lower()
	freqdict = dict()
	pattern = re.compile(r"([A-Za-z]+)")
	for word in re.findall(pattern, string):
		if word in freqdict:
			freqdict[word] += 1
		else:
			freqdict[word] = 1
	words=[]
	outfile = open('onewordfreq','wb')
	for word in sorted(freqdict, key=freqdict.get, reverse=True):
		words.append((freqdict[word],word))
	pickle.dump(words, outfile)
	outfile.close()
		


def multiWordFrequency(txt, n):#train model and read corpus
	answer = ()
	pattern = re.compile(r"([A-Za-z]+)")
	with codecs.open(txt, 'r', 'utf-8') as file:
		for line in file:
			line = line.lower()
			answer = answer + tuple(re.findall(pattern, line))
	model = dict()
	for i in range(len(answer)-n+1):
		key = answer[i:i+n-1]
		val = answer[i+n-1]
		if key in model:
			if val in model[key]:
				model[key][val] += 1
			else:
				model[key][val] = 1
		else:
			model[key] = dict()
			model[key][val] = 1
	outfile = open('multiwordfreq', 'wb')
	pickle.dump(model, outfile)
	outfile.close()

#singleWordFrequency('big.txt')
#multiWordFrequency('big.txt',3)
