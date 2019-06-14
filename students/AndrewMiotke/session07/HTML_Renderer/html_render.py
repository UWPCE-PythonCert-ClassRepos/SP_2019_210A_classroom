#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class TextWrapper:
    def __init__(self, text):
        self.text = text


    def render(self, file_out, current_indent = ""):
        file_out.write(current_indent + self.text)


# This is the framework for the base class
class Element: # Did we need the () in Python3+ ?

    tag = 'html'
    indent = "    "


    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)


    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))


    def make_tags(self):
        attributes = " ".join([f'{key}="{val}' for key, val in self.attributes.items()])

        if attributes.strip():
            open_tag = f"<{self.tag} {attributes.strip()}>"
        else:
            open_tag = f"<{self.tag}>"

        close_tag = f"</{self.tag}>"

        return open_tag, close_tag


    def render(self, out_file, current_indent = ""):
        open_tag, close_tag = self.make_tags()
        out_file.write(current_indent + open_tag + "\n")

        for stuff in self.content:
            stuff.render(out_file, current_indent + self.indent)
            out_file.write("\n")

        out_file.write(current_indent + close_tag)


class OneLineTag(Element):

    def render(self, out_file, current_indent = ""):
        open_tag, close_tag = self.make_tags()
        out_file.write(current_indent + open_tag)

        for stuff in self.content:
            stuff.render(out_file)

        out_file.write(close_tag)


class Html(Element):
    tag = 'html'

    def render(self, file_out, current_indent = ""):
        file_out.write(current_indent + "!DOCTYPE html\n")
        super().render(file_out, current_indent=current_indent)


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = 'title'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class SelfClosingTag(Element):

    def append(self, *args, **kwargs):
        raise TypeError("Content can't be added to a self closing tag")


    def render(self, out_file, indentation = ""):
        open_tag, _ = self.make_tags()
        out_file.write(indentation + open_tag.replace(">", "/>"))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs["href"] = link
        super().__init__(*args, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, level, *args, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"