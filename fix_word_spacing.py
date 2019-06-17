import json

with open("words_dictionary.json") as wd:
    words = json.load(wd)

# this is a list of english words from https://github.com/dwyl/english-words

words = set(words.keys())


def find_split(testword):
    for x in range(1, len(testword)):
        first = testword[0:x]
        second = testword[x:]
        if (first in words) or (first.lower() in words):
            if (second in words) or (second.lower() in words):
                return x
    return False

def split_word(inword):
    word = inword.strip()
    lower = word.lower()
    if (word in words) or (lower in words):
        return inword
    split_index = find_split(word)
    if split_index:
        correction = inword[0:split_index] + " " + inword[split_index:]
        return correction
    return inword

def correct_line(line):
    if len(line) == 1:
        return line
    words = line.split(" ")
    for word in words:
        correction = split_word(word)
        if correction != word:
            print(word)
            print(correction)

sample_line = """In 1992, California enacted a statute limiting the maximum welfare benefitsavailable to newly arrived residents. The scheme limits the amount payable toa family that has resided in the State for less than 12 months to the amountpayable by the State of the family's prior residence. The questions presentedby this case are whether the 1992 statute was constitutional when it wasenacted and, if not, whether an amendment to the Social Security Act enactedby Congress in 1996 affects that determination.
"""

correct_line(sample_line)

# with open("saenz.md") as saenzin:
#     lines = saenzin.readlines()

# out = []

# for line in lines:
#     if len(line) == 1:
#         out.append(line)
#     else:
#         words = line.split(" ")
        # fixedline = " ".join([split_word(x) for x in words])
        # out.append(fixedline)

# text = "".join(out)
# print(text)

#with open("saenz2.md", "w") as saenzout:
#    lines = saenzin.readlines()

# THIS DOESN'T WORK RIGHT because the wordlist is too short.  It misses words like "constitution." and "court"
