import pickle

infile = open('onewordfreq','rb')
new_dict=pickle.load(infile)
infile.close()

def error(word):
	f = open('onewordfreq','rb')
	words = pickle.load(f)
	f.close()
	for i in words:
		if i[1] == word:
			return i[0]
	return 0

infile = open('multiwordfreq','rb')
new_dict=pickle.load(infile)
infile.close()

def languagemodel(words, word):
	#if len(words.split())==2:
	f = open('multiwordfreq','rb')
	new_dict=pickle.load(f)
	f.close()
	w = tuple(words.split())
	choices = new_dict.get(w)
	if choices.get(word)==None:
		freq = 0
	else:
		freq = choices.get(word)
	#print(freq)
	#if freq == None:
		#freq=0
	return freq

#print(languagemodel('this is','wrong'))

