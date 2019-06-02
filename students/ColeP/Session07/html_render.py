#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):

        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents:
        open_tag = ["<{}".format(self.tag)]
        for key in self.kwargs:
            open_tag.append(" "+key+"=")
            open_tag.append('"'+self.kwargs[key]+'"')
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        # tried the following first, so close but so far
        # out_file.write("<{}{}>\n".format(self.tag, str(self.kwargs).strip("{}")))  # .replace("'", " ")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>".format(self.tag))


class Body(Element):
    tag = 'body'


class Html(Element):
    tag = 'html'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("</{}>".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTab(Element):
    pass


class Hr(SelfClosingTab):
    tag = 'hr'

    def render(self, outfile):
        tag = "<{}".format(self.tag) + " />\n"
        outfile.write(tag)


class Br(SelfClosingTab):
    tag = 'Br'

