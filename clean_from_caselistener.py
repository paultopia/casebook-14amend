import sys


def fix_lines(linelist):
    paragraphs = []
    for line in lines:
        cleanedline = line.strip()
        if cleanedline.isnumeric():
            paragraphs.append("\n\n")
        else:
            paragraphs.append(cleanedline + " ")
            # this is a slight bug, adds line at end of blank lines, hence leading space in paragraphs. 
    text = "".join(paragraphs)
    return text


try:
    filename = sys.argv[1]
    with open(filename) as s:
        lines = s.readlines()
    text = fix_lines(lines)
    with open(filename, "w") as s:
        s.write(text)
except:
    print("unable to open file. did you pass the right filename to command?")
