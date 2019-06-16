with open("saenz.md") as s:
    lines = s.readlines()

paragraphs = []
for line in lines:
    cleanedline = line.strip()
    if cleanedline.isnumeric():
        paragraphs.append("\n\n")
    else:
        paragraphs.append(cleanedline)

text = "".join(paragraphs)

with open("saenz.md", "w") as s:
    s.write(text)
