import re

with open("problems_cleaned.md", encoding="utf-8") as infile:
     text = infile.readlines()

def is_more_than_one_char(line):
    return len(line.strip()) > 1

def not_just_numbers_and_dots(line):
    cleanline = line.replace(".", "")
    cleanerline = re.sub("\s+", "", cleanline)
    return not cleanerline.isnumeric()


text2 = list(filter(lambda x: is_more_than_one_char(x) and not_just_numbers_and_dots(x), text))

the_string = "\n\n".join([x.strip() for x in text2])

replace_with_newlines = [r"\s+I{2,}\s+",
                         r"\sVI+\s+",
                         r"\sXI+\s+"]

for pattern in replace_with_newlines:
    the_string = re.sub(pattern, "\n\n", the_string)

us_code_cite = r",\s\d+\sU\.\s?S\.\s\d+,?\s?\d+[-\s]?\(?\d{0,4}\)?"

f_2d_cite = r"\d+\sF\.\s?2d\s\d+,?\s?\d*\s?\(?\d{0,4}\)?"

replace_with_empty_string = [us_code_cite, f_2d_cite]

for pattern in replace_with_empty_string:
    the_string = re.sub(pattern, "", the_string)


ante = r"\s[Aa]nte,\s?at\s\d+-?\d*\.?,?\s?\d*\.?"

idcite = r"\s[iI]d\.,?\s(at)?\s?\d*"

ibid = r"\\s[iI]bid\\.\\s"

anteat = r"\s[Aa]nte, at \d+\.\s"

replace_with_space = [ante, idcite, ibid, anteat]

for pattern in replace_with_space:
    the_string = re.sub(pattern, " ", the_string)


def replace_dots_with_dashes(string):
    return string.replace("•", "-")

def replace_weird_fucked_apostrophes(string):
    return string.replace(" `", "'")


outdoc = replace_dots_with_dashes(replace_weird_fucked_apostrophes(the_string))

with open("second_problems_cleaned.md", "w", encoding="utf-8") as outfile:
     outfile.write(outdoc)
