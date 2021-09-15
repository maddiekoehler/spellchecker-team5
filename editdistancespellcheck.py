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
            

def isRealWords(words):
    realWordsList = open('big.txt').read()
    realWords = []
    for w in words:
        if w in realWordsList:
            realWords.append(w)
    return realWords



print(isRealWords(oneEditDist('cay')+twoEditDist('cay')))
