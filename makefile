latex = pdflatex --synctex=1 --interaction=nonstopmode $(1).tex < /dev/null
bibtex = bibtex $(1).aux

all:
	$(call latex,moivre_laplace_theorem)
	bibtex moivre_laplace_theorem.aux
	$(call latex,moivre_laplace_theorem)
	$(call latex,moivre_laplace_theorem)
