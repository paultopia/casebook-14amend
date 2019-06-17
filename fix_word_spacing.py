import json

with open("words_dictionary.json") as wd:
    words = json.load(wd)

# this is a list of english words from https://github.com/dwyl/english-words

words = set(words.keys())

def find_split(testword):
    for x in range(1, len(testword)):
        first = testword[0:x]
        second = testword[x:]
        if (first in words) and (second in words):
            return x
    return False

def split_word(inword):
    word = inword.lower()
    if word in words:
        return inword
    print(word)
    split_index = find_split(word)
    if split_index:
        correction = inword[0:split_index] + " " + inword[split_index:]
        print(correction)
        return correction
    return inword

with open("saenz.md") as saenzin:
    lines = saenzin.readlines()

out = []

for line in lines:
    if len(line) == 1:
        out.append(line)
    else:
        words = line.split(" ")
        fixedline = " ".join([split_word(x) for x in words])
        out.append(fixedline)

#text = "".join(out)
#print(text)

#with open("saenz2.md", "w") as saenzout:
#    lines = saenzin.readlines()

# THIS DOESN'T WORK RIGHT because the wordlist is too short.  It misses words like "constitution." and "court"
