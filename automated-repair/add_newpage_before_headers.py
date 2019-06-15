with open("working-copy.md") as f:
    lines = f.readlines()

newpage = r"""

\newpage

"""

paragraphs = []

for x in lines:
    if x.startswith("#"):
        paragraphs.append(newpage + x)
    else:
        paragraphs.append(x)

with open("working-copy-newpages.md", "w") as out:
    out.write("".join(paragraphs))

