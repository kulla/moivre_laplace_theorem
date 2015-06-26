MAIN    = moivre_laplace_theorem
SOURCES = $(wildcard *.tex)

latex   = pdflatex -halt-on-error -synctex=1 -interaction=nonstopmode $(1).tex < /dev/null;

all: pdf

pdf: ${MAIN}.pdf

${MAIN}.pdf: ${SOURCES}
	$(call latex,${MAIN})
	bibtex ${MAIN}.aux
	while ( grep "Rerun to get cross-references" ${MAIN}.log > /dev/null ); do \
		$(call latex,${MAIN}) \
	done
