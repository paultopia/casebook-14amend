import re

with open("headings_added.md", encoding="utf-8") as infile:
    text = infile.readlines()


# with open("problem-samples.txt", encoding="utf-8") as infile:
#     text = infile.readlines()

def fix_bad_paragraphs(line):
    if line.startswith("\xa0"):
        nostarter = re.sub("^\xa0+", "", line)
        return nostarter
    return False

floating_string = ""

paragraphs = []

for line in text:
    hanging = fix_bad_paragraphs(line)
    if hanging:
        floating_string = hanging
    else:
        if line.isspace():
            paragraphs.append(line)
        else:
            if floating_string:
                newline = floating_string.strip() + " " + line
                paragraphs.append(newline)
                floating_string = ""
            else:
                paragraphs.append(line)

no_single_chars = [x for x in paragraphs if len(x.strip()) != 1]

no_just_numeric = [x for x in no_single_chars if not x.strip().isnumeric()]

fulltext = "".join(no_just_numeric)

period_cite = r"\.\s+\n+\[\d+\sU\.S\.\s\d+\]\s+\n+"

cleaned = re.sub(period_cite, ".\n\n\n", fulltext)

no_period_cite = r"\s+\[\d+\sU\.S\.\s\d+\]\s+\n+"

more_cleaned = re.sub(no_period_cite, " ", cleaned)

no_star_pages = re.sub(r"\*\d+", "", more_cleaned)

asterisk_omissions = r"\*\s?\*\s?\*\s+"

no_star_pages = re.sub(asterisk_omissions, "\n\n", no_star_pages)

pagelines_caps = r"\s*Page\s\d+\s+([A-Z])"

no_pagelines_caps = re.sub(pagelines_caps, "\n\n\\1", no_star_pages)

pagelines_lower = r"\s*Page\s\d+\s+([a-z])"

no_pagelines = re.sub(pagelines_lower, " \\1", no_pagelines_caps)

only_two_linebreaks = re.sub(r"\n{2,}", "\n\n", no_pagelines)

no_horrid_latin1_spaces = re.sub("\xa0+", " ", only_two_linebreaks)

with open("problems_cleaned.md", "w", encoding="utf-8") as outfile:
    outfile.write(no_horrid_latin1_spaces)
