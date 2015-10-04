MAIN     = moivre_laplace_theorem
SOURCES  = $(wildcard *.tex)

FIGURES  = $(patsubst %.svg,%.pdf,$(wildcard ./figures/*.svg)) \
	   $(patsubst %.jpg,%.pdf,$(wildcard ./figures/*.jpg)) \
	   $(patsubst %.png,%.pdf,$(wildcard ./figures/*.png))

latex = pdflatex -halt-on-error -synctex=1 -interaction=nonstopmode $(1).tex < /dev/null;

all: pdf

pdf: ${MAIN}.pdf

${MAIN}.pdf: ${SOURCES} ${FIGURES}
	$(call latex,${MAIN})
	makeglossaries ${MAIN}
	bibtex ${MAIN}.aux
	$(call latex,${MAIN})
	$(call latex,${MAIN})

figures/%.pdf: figures/%.svg
	inkscape --export-area-drawing --export-pdf=$@ $<

figures/%.pdf: figures/%.jpg
	convert $< $@

figures/%.pdf: figures/%.png
	convert $< $@

clean:
	git -fx
