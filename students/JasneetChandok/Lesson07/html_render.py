#!/usr/bin/env python3

"""
A class-based system for rendering html.

Written By: Jasneet Chandok
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    # def render(self, out_file):
    #     out_file.write("<{}>\n".format(self.tag))
    #     for contents in self.content:
    #         out_file.write(contents + "\n")
    #     out_file.write("</{}>\n".format(self.tag))

    def render(self, out_file):
        # loop through the list of contents:
        for contents in self.content:
            out_file.write("<{}>\n".format(self.tag))
            try:
                contents.render(out_file)
            except AttributeError:
                out_file.write(contents)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.content[0])
        out_file.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def append(self, *args, **kwargs):
        raise TypeError("You can not add content to a self closing tag")

    def render(self, out_file):
        # loop through the list of contents:
        for contents in self.content:
            out_file.write("<{}>\n".format(self.tag))
            try:
                contents.render(out_file)
            except AttributeError:
                out_file.write(contents)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
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
