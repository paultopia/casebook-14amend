

with open("better_linebreaks_removed.txt", encoding="utf-8") as et:
    text = et.readlines()


def is_blank(line):
    if line.isspace():
        return True
    if "[ … ]" in line:
        return True
    else:
        return False
            
paragraphs = [x for x in text if not is_blank(x)]

with open("extra_newlines_removed.txt", "w", encoding="utf-8") as out:
    out.write("\n\n".join(paragraphs))
