# python-epub2

`epub2.py` allows you to create EPUB2 files easily in Python scripts.  
See [examples](examples/) for code snippets.

## Requirements

- Python 3
- Jinja2

## Documentation

- `epub2.EpubBuilder`
- `epub2.EpubMetadata`
- `epub2.EpubNavPoint`

## Installation via pip

```bash
# user install
pip install -e git://github.com/yapper-git/python-epub2.git#egg=python-epub2 --user
# default install
pip install -e git://github.com/yapper-git/python-epub2.git#egg=python-epub2
```

## EPUB Reminder

- **manifest**: list of the files in the .epub container, and their file type
- **spine**: list the reading order of the contents (i.e. the XHTML files, no images)
- **toc.ncx**: the table of contents

## EPUB on Wikipedia

> EPUB (short for electronic publication; alternatively capitalized as ePub,
> ePUB, EPub, or epub, with "EPUB" preferred by the vendor) is a free and open
> e-book standard by the International Digital Publishing Forum (IDPF). Files
> have the extension .epub.
> 
> EPUB is designed for reflowable content, meaning that an EPUB reader can
> optimize text for a particular display device. EPUB also supports fixed-layout
> content. The format is intended as a single format that publishers and
> conversion houses can use in-house, as well as for distribution and sale. It
> supersedes the Open eBook standard.

## External links

- [Open Packaging Format (OPF) 2.0.1 v1.0.1 (Drafts)](http://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2)
- [Documentation of Python-Epub (French)](http://epub.exirel.me/epub/opf.html)
