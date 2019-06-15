import re

with open("second_problems_cleaned.md", encoding="utf-8") as infile:
    text = infile.read()

us_reporter_cite_again = r"\,\s\d+\sU\.\s?S\.,\sat\s\d+-?\d*"

l_ed_cite = r"\d+\sL\.\s?Ed\.\s?(2d)?\s(at\s)?\d+\s?(\(\d\d\d\d\))?"

s_ct_cite = r",?\d{0,4}\s?S\.\s?Ct\.,?\s(at)?\d*,?\s?\d*-?\d*[,\.]\s"

f_3d_cite = r"\d+\sF\.\s?3d\s\d+,?\s?\d*\s?\(?\d{0,4}\)?"

replace_with_empty_string = [us_reporter_cite_again, l_ed_cite, s_ct_cite, f_3d_cite]

for pattern in replace_with_empty_string:
    text = re.sub(pattern, "", text)

probable_paragraph_footnote_markers = [r"\d+\n", r"\[\d+\]\n"]

for pattern in probable_paragraph_footnote_markers:
    text = re.sub(pattern, "\n", text)

probable_inline_footnote_markers = [r"\.\[\d+\]", "\.\d+"]

for pattern in probable_inline_footnote_markers:
    text = re.sub(pattern, " ", text)

probable_page_markers = [r"\s\[\d+\]\s"]

for pattern in probable_page_markers:
    text = re.sub(pattern, " ", text)

probable_quote_footnotes = [r"(')\d\s", r'(\")\d\s']

for pattern in probable_quote_footnotes:
    text = re.sub(pattern, "\\1 ", text)

text = text.replace("''", '"')

with open("third_problems_cleaned.md", "w", encoding="utf-8") as outfile:
    outfile.write(text)
