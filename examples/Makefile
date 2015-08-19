EPUB_FILES   = $(patsubst %.py,%.epub,$(wildcard *.py))
EPUB_FOLDERS = $(patsubst %.py,%.epub-FILES,$(wildcard *.py))

export PYTHONPATH := $(realpath ..)

all: $(EPUB_FILES) $(EPUB_FOLDERS)

%.epub: %.py
	python $<
	-epubcheck $@

%.epub-FILES: %.epub
	rm -rf $@
	unzip -o $< -d $@

clean:
	rm -rf *.epub-FILES

mrproper: clean
	rm -f *.epub

.PHONY: clean mrproper
