import re

with open("old/third_problems_cleaned.md", encoding="utf-8") as infile:
    text = infile.read()

supra = r",?\s?supra,?\s?(at)?\s?[\d\-]*"

at = r",?\sat\s?\d+-?\d*"

another_likely_fn = r",\[\d+\]"

another_us_reporter = r"\d+\sU\.\s?S\.,\ at\ \d+\.?"

more_federal_reporter = r",?\s\d+\sF.\s?[23]d\.?,?\ (at\s)?\d+"

loose_numbers = r"[—-]\d+\,\s\d+[—-]?\s?\d*"

another_s_ct = r"\d+\sS\.\s?Ct\.,?\s(at)?\s?\d+"

blank_us_cite = r"\d+\sU\.\s?S\.,?\ at\ ?_+"

more_l_ed = r"\d+\sL\.\s?ed\.\s\d+,?\s?\d*"

old_s_ct = r"Sup\.\s?Ct\.\s?Rep\.\sp?\.?\s?\d+,?\s?\d*"

f_supp_pincite = r"\d+\sF\.\s?Supp\.\s?(2d)?\s?,?\sat\s\d+"

another_likely_footnote = r";\d+"

replace_with_empty_string = [supra, at,
                             another_likely_fn,
                             another_us_reporter,
                             loose_numbers,
                             more_federal_reporter,
                             another_s_ct,
                             r"IV\n\n",
                             r"IX\n\n",
                             blank_us_cite,
                             old_s_ct,
                             more_l_ed,
                             f_supp_pincite,
                             another_likely_footnote]

for pattern in replace_with_empty_string:
    text = re.sub(pattern, "", text)

text = text.replace("\n ", "\n\n")

text = text.replace(" , ", " ")

text = text.replace(" . ", " ")

text = text.replace(" .\n", "\n")

with open("fourth_problems_cleaned.md", "w", encoding="utf-8") as outfile:
    outfile.write(text)
