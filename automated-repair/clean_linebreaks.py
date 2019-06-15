paragraphs = []

with open("uncleaned.txt") as et:
    text = et.readlines()

# print(text)

def has_latin_tabs(line):
    return line.startswith("\xa0\xa0")

# print([has_latin_tabs(x) for x in text])

def is_blank(line):
    if line.isspace():
        return True
    if "[ … ]" in line:
        return True
    else:
        return False

def is_line_ending(index, line):
    try:
        nextline = text[index + 1]
    except:
        return True
    if is_blank(nextline) or has_latin_tabs(nextline):
        return True
    if len(line) < 45:
        return True
    return False


current_paragraph = ""
for idx, line in enumerate(text):
    if is_line_ending(idx, line):
        if not is_blank(line):
            current_paragraph += line
        current_paragraph += "\n\n"
        paragraphs.append(current_paragraph.replace("\n", " "))
        current_paragraph = ""
    else:
        if not is_blank(line):
            current_paragraph += line


with open("linebreaks_removed.txt", "w") as out:
    out.write("\n\n".join(paragraphs))
