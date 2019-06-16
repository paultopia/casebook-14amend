all: commit

commit: build
	git add .
	git commit -m "compile a draft"
	git push

build: working-copy.md
	pandoc -s -o testbuild.pdf --pdf-engine=xelatex working-copy.md
