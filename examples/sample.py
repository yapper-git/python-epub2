from epub2 import EpubBuilder, EpubNavPoint

epub = EpubBuilder("sample.epub")
epub.open()

epub.identifier = "sample"
epub.title = "Sample ePUB file"

epub.metadata.add_title("Title N°2")
epub.metadata.add_title("Title N°3")
epub.metadata.add_creator("Creator N°1")
epub.metadata.add_creator("Creator N°2", role="aut")
epub.metadata.add_creator("Creator N°3", file_as="Creator 3", role="oth")
epub.metadata.add_subject("Subject N°1")
epub.metadata.add_subject("Subject N°2")
epub.metadata.set_description("Description")
epub.metadata.set_publisher("Publisher")
epub.metadata.add_contributor("Contributor N°1")
epub.metadata.add_contributor("Contributor N°2", role="aut")
epub.metadata.add_contributor("Contributor N°3", file_as="Contributor 3", role="oth")
epub.metadata.add_date("2014")
epub.metadata.add_date("2014-12", event="modification")
epub.metadata.add_date("2014-12-25", event="publication")
epub.metadata.set_type("type")
epub.metadata.set_format("format")
epub.metadata.add_identifier("uuid002")
epub.metadata.add_identifier("uuid003", "myid", "scheme")
epub.metadata.set_source("source")
epub.metadata.add_language("en-US")
epub.metadata.add_language("fr-fr")
epub.metadata.add_language("de")
epub.metadata.set_relation("relation")
epub.metadata.set_coverage("coverage")
epub.metadata.set_rights("rights")
epub.metadata.add_meta("name1", "content1")
epub.metadata.add_meta("name2", "content2")

epub.add_guide(type="title-page", title="Title page", href="texts/titlepage.xhtml")
epub.add_guide(type="toc", title="Table of Contents", href="texts/contents.xhtml")

epub.add_navpoint(EpubNavPoint("chap1", "Chapter 1", "texts/chapter1.xhtml"))
epub.add_navpoint(EpubNavPoint("chap2", "Chapter 2", "texts/chapter2.xhtml"))

epub.add_text_from_string(id="titlepage", localname="texts/titlepage.xhtml", content="""\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
    <title>Sample ePUB file</title>
    <link rel="stylesheet" href="../styles/stylesheet.css" type="text/css"/>
  </head>
  <body>
    <h1>Sample ePUB file</h1>
  </body>
</html>""")

epub.add_text_from_string(id="contents", localname="texts/contents.xhtml", content="""\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
    <title>Tables of Contents</title>
    <link rel="stylesheet" href="../styles/stylesheet.css" type="text/css"/>
  </head>
  <body>
    <h1>Table of Contents</h1>
    <ol>
      <li><a href="chapter1.xhtml">Chapter 1</a></li>
      <li><a href="chapter2.xhtml">Chapter 2</a></li>
    </ol>
  </body>
</html>""")

epub.add_text_from_string(id="chap1", localname="texts/chapter1.xhtml", content="""\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
    <title>Chapiter 1</title>
    <link rel="stylesheet" href="../styles/stylesheet.css" type="text/css"/>
  </head>
  <body>
    <h1>Chapter 1</h1>
    <p>Et eodem impetu Domitianum praecipitem per scalas itidem funibus
    constrinxerunt, eosque coniunctos per ampla spatia civitatis acri raptavere
    discursu. iamque artuum et membrorum divulsa conpage superscandentes corpora
    mortuorum ad ultimam truncata deformitatem velut exsaturati mox abiecerunt
    in flumen.</p>
    <p>Illud autem non dubitatur quod cum esset aliquando virtutum omnium
    domicilium Roma, ingenuos advenas plerique nobilium, ut Homerici bacarum
    suavitate Lotophagi, humanitatis multiformibus officiis retentabant.</p>
    <p>Procedente igitur mox tempore cum adventicium nihil inveniretur, relicta
    ora maritima in Lycaoniam adnexam Isauriae se contulerunt ibique densis
    intersaepientes itinera praetenturis provincialium et viatorum opibus
    pascebantur.</p>
  </body>
</html>""")

epub.add_text_from_string(id="chap2", localname="texts/chapter2.xhtml", content="""\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
    <title>Chapter 2</title>
    <link rel="stylesheet" href="../styles/stylesheet.css" type="text/css"/>
  </head>
  <body>
    <h1>Chapter 2</h1>
    <p><img src="../images/logo.png" alt="ePUB Logo"/></p>
    <ul>
      <li>Proinde concepta rabie saeviore, quam desperatio</li>
      <li>Illud autem non dubitatur quod cum esset aliquando</li>
      <li>Nam sole orto magnitudine angusti gurgitis sed</li>
      <li>Quare hoc quidem praeceptum, cuiuscumque est, ad</li>
      <li>Cumque pertinacius ut legum gnarus accusatorem</li>
    </ul>
  </body>
</html>""")

epub.add_style_from_string("styles/stylesheet.css", """\
h1 {
    color: gray;
    border-bottom: 1px solid gray;
}

p:first-letter {
    font-size: 1.8em;
    float: left;
}""", "style")

epub.add_file_from_file("images/logo.png", "sample-logo.png", "logo", "image/png")

epub.close()
