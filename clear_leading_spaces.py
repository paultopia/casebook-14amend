import sys


def fix_spaces(linelist):
    paragraphs = []
    for line in lines:
        if line[0] == " ":
            cleanedline = line[1:]
        else:
            cleanedline = line
        paragraphs.append(cleanedline)
    text = "".join(paragraphs)
    return text


try:
    filename = sys.argv[1]
    with open(filename) as s:
        lines = s.readlines()
    text = fix_spaces(lines)
    with open(filename, "w") as s:
        s.write(text)
except:
    print("unable to open file. did you pass the right filename to command?")
