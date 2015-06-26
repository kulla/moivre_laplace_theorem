main_tex_file = moivre_laplace_theorem

latex = pdflatex --synctex=1 --interaction=nonstopmode $(1).tex < /dev/null
bibtex = bibtex $(1).aux

all:
	$(call latex,$(main_tex_file))
	bibtex $(main_tex_file).aux
	$(call latex,$(main_tex_file))
	$(call latex,$(main_tex_file))
