from epub2 import EpubBuilder, EpubNavPoint

epub = EpubBuilder("contents.epub")

epub.identifier = "contents"
epub.title = "Deep Table of Contents"

epub.metadata.add_language("en")

toc1 = EpubNavPoint("toc.1", "1. Chapter 1", "text.html#toc.1")
toc2 = EpubNavPoint("toc.2", "2. Chapter 2", "text.html#toc.2")
toc3 = EpubNavPoint("toc.3", "3. Chapter 3", "text.html#toc.3")
epub.add_navpoint(toc1)
epub.add_navpoint(toc2)
epub.add_navpoint(toc3)

toc11 = EpubNavPoint("toc.1.1", "1.1. Section 1", "text.html#toc.1.1")
toc12 = EpubNavPoint("toc.1.2", "1.2. Section 2", "text.html#toc.1.2")
toc1.append(toc11)
toc1.append(toc12)

toc21 = EpubNavPoint("toc.2.1", "2.1. Section 1", "text.html#toc.2.1", [
    EpubNavPoint("toc.2.1.1", "2.1.1. Subsection 1", "text.html#toc.2.1.1"),
    EpubNavPoint("toc.2.1.2", "2.1.2. Subsection 2", "text.html#toc.2.1.2"),
    EpubNavPoint("toc.2.1.3", "2.1.3. Subsection 3", "text.html#toc.2.1.3")
])
toc22 = EpubNavPoint("toc.2.2", "2.2. Section 2", "text.html#toc.2.2")
toc2.append(toc21)
toc2.append(toc22)

epub.open()

epub.add_text_from_string(id="text", localname="text.html", content="""\
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
    <title>Deep Table of Contents</title>
  </head>
  <body>
    <h1 id="toc.1">1. Chapter 1</h1>
    <h2 id="toc.1.1">1.1. Section 1</h2>
    <h2 id="toc.1.2">1.2. Section 2</h2>
    <h1 id="toc.2">2. Chapter 2</h1>
    <h2 id="toc.2.1">2.1. Section 1</h2>
    <h3 id="toc.2.1.1">2.1.1. Subsection 1</h3>
    <h3 id="toc.2.1.2">2.1.2. Subsection 2</h3>
    <h3 id="toc.2.1.3">2.1.3. Subsection 3</h3>
    <h2 id="toc.2.2">2.2. Section 2</h2>
    <h1 id="toc.3">3. Chapter 3</h1>
  </body>
</html>""")

epub.close()
