MAIN     = moivre_laplace_theorem
SOURCES  = $(wildcard *.tex)

SVG_FIGURES = $(patsubst %.svg,%.pdf,$(wildcard ./figures/*.svg))

latex = pdflatex -halt-on-error -synctex=1 -interaction=nonstopmode $(1).tex < /dev/null;

all: pdf

pdf: ${MAIN}.pdf

${MAIN}.pdf: ${SOURCES} ${SVG_FIGURES}
	$(call latex,${MAIN})
	bibtex ${MAIN}.aux
	while ( grep "Rerun to get cross-references" ${MAIN}.log > /dev/null ); do \
		$(call latex,${MAIN}) \
	done

figures/%.pdf: figures/%.svg
	inkscape --export-area-drawing --export-pdf=$@ $<
