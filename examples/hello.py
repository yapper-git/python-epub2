from epub2 import EpubBuilder, EpubNavPoint

with EpubBuilder("hello.epub") as epub:

    epub.identifier = "helloworld"
    epub.title = "Hello world!"

    epub.metadata.add_language("en")

    epub.add_text_from_file("texts/hello.xhtml", "hello.html", "hello")

    epub.add_navpoint(EpubNavPoint("hello", "Hello", "texts/hello.xhtml"))
