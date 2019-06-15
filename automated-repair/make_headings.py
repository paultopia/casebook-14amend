headings_list = ["Procedural Due Process",
                 "Substantive Due Process",
                 "From Due Process to Equal Protection",
                 "Equal Protection",
                 "Gay Rights at the Intersection of Substantive Due Process and Equal Protection",
                 "Congress's Enforcement Power"]
subheadings_list = ["Incorporation",
                    "Fundamental Rights",
                    "Foundations, and Race",
                    "Gender and Intermediate Scrutiny"]

with open("caselist.txt") as cases:
    cases_list = [x.strip() for x in cases.readlines() if not x.isspace()]


def make_heading(line):
    stripline = line.strip()
    if stripline in headings_list:
        return "# " + line
    if stripline in subheadings_list:
        return "## " + line
    if stripline in cases_list:
        return "### " + line
    return line

with open("extra_newlines_removed.txt", encoding="utf-8") as infile:
    text = infile.readlines()

out_lines = [make_heading(x) for x in text]

with open("headings_added.md", "w", encoding="utf-8") as out:
    out.write("".join(out_lines))
