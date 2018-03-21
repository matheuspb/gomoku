all: relatorio-1.pdf

relatorio-1.pdf: relatorio-1.tex relatorio-1.bib
	pdflatex relatorio-1.tex
	bibtex relatorio-1.aux
	pdflatex relatorio-1.tex
	pdflatex relatorio-1.tex

clean:
	@rm -f relatorio-1.pdf *.aux *.bbl *.blg *.log
