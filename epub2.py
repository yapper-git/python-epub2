from jinja2 import Environment, FileSystemLoader
import os
from zipfile import ZipFile


class EpubBuilder:
    """EpubBuilder creates an ePUB2 file"""

    def __init__(self, file_path):
        self.identifier = None
        self.title = None
        self.metadata = EpubMetadata()
        self.navpoints = []
        self.manifest = []
        self.spine = []
        self.guide = []

        templates_folder = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'templates'
        )
        self.env = Environment(loader=FileSystemLoader(templates_folder))

        self._file_path = file_path
        self.add_manifest("ncx", "toc.ncx", "application/x-dtbncx+xml")

    def open(self):
        self._zip = ZipFile(self._file_path, "w")
        self._write_mimetype_file()
        self._write_container_file()

    def close(self):
        self._write_opf_file()
        self._write_ncx_file()
        self._zip.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def add_navpoint(self, navpoint):
        self.navpoints.append(navpoint)

    def add_manifest(self, id, href, media_type):
        self.manifest.append({
            "id": id, "href": href, "media-type": media_type
        })

    def add_spine(self, idref, linear=True):
        self.spine.append({"idref": idref, "linear": linear})

    def add_guide(self, type, title, href):
        self.guide.append({"type": type, "title": title, "href": href})

    def add_file_from_file(self, localname, filename, id, media_type):
        self._zip.write(filename, "OEBPS/" + localname)
        self.add_manifest(id, localname, media_type)

    def add_file_from_string(self, localname, content, id, media_type):
        self._zip.writestr("OEBPS/" + localname, content)
        self.add_manifest(id, localname, media_type)

    def add_text_from_file(self, localname, filename, id):
        self.add_file_from_file(
            localname, filename, id, "application/xhtml+xml"
        )
        self.add_spine(id)

    def add_text_from_string(self, localname, content, id):
        self.add_file_from_string(
            localname, content, id, "application/xhtml+xml"
        )
        self.add_spine(id)

    def add_style_from_file(self, localname, filename, id):
        self.add_file_from_file(localname, filename, id, "text/css")

    def add_style_from_string(self, localname, content, id):
        self.add_file_from_string(localname, content, id, "text/css")

    def _write_mimetype_file(self):
        self._zip.writestr("mimetype", "application/epub+zip")

    def _write_container_file(self):
        template = self.env.get_template("container.xml")
        template_render = template.render()
        self._zip.writestr("META-INF/container.xml", template_render)

    def _write_opf_file(self):
        template = self.env.get_template("content.opf")
        template_render = template.render(
            identifier=self.identifier,
            title=self.title,
            metadata=self.metadata,
            manifest=self.manifest,
            spine=self.spine,
            guide=self.guide,
        )
        self._zip.writestr("OEBPS/content.opf", template_render)

    def _write_ncx_file(self):
        template = self.env.get_template("toc.ncx")
        template_render = template.render(
            uid=self.identifier,
            title=self.title,
            depth=self._depth(),
            navpoints=self.navpoints
        )
        self._zip.writestr("OEBPS/toc.ncx", template_render)

    def _depth(self):
        self._max_depth = -1
        self._current_depth = 0
        self._depth_recursive(self.navpoints)
        return self._max_depth

    def _depth_recursive(self, navpoints):
        for child_navpoint in navpoints:
            self._current_depth += 1
            if self._current_depth > self._max_depth:
                self._max_depth = self._current_depth
            self._depth_recursive(child_navpoint.children)
            self._current_depth -= 1


class EpubMetadata:
    """EpubMetadata represents the metadata element in .opf file"""

    def __init__(self):
        self.titles = []
        self.creators = []
        self.subjects = []
        self.description = None
        self.publisher = None
        self.contributors = []
        self.dates = []
        self.type = None
        self.format = None
        self.identifiers = []
        self.source = None
        self.languages = []
        self.relation = None
        self.coverage = None
        self.rights = None
        self.metas = []

    def add_title(self, title):
        self.titles.append(title)

    def add_creator(self, name, role=None, file_as=None):
        self.creators.append({"name": name, "role": role, "file-as": file_as})

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_description(self, description):
        self.description = description

    def set_publisher(self, publisher):
        self.publisher = publisher

    def add_contributor(self, name, role=None, file_as=None):
        self.contributors.append({
            "name": name, "role": role, "file-as": file_as
        })

    def add_date(self, date, event=None):
        self.dates.append({"date": date, "event": event})

    def set_type(self, type):
        self.type = type

    def set_format(self, format):
        self.format = format

    def add_identifier(self, content, id=None, scheme=None):
        self.identifiers.append({
            "content": content, "id": id, "scheme": scheme
        })

    def set_source(self, source):
        self.source = source

    def add_language(self, language):
        self.languages.append(language)

    def set_relation(self, relation):
        self.relation = relation

    def set_coverage(self, coverage):
        self.coverage = coverage

    def set_rights(self, rights):
        self.rights = rights

    def add_meta(self, name, content):
        self.metas.append({"name": name, "content": content})


class EpubNavPoint:
    """EpubNavPoint represents a NavPoint element for contents"""

    def __init__(self, id=None, label=None, source=None, children=None):
        self.id = id
        self.label = label
        self.source = source
        self.children = children if children else []

    def append(self, navpoint):
        self.children.append(navpoint)
