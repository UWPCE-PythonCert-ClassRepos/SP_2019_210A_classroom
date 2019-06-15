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

    # def render(self, out_file):
    #     # loop through the list of contents:
    #     out_file.write(self._open_tag())
    #     out_file.write("\n")
    #     for content in self.contents:
    #         try:
    #             content.render(out_file)
    #         except AttributeError:
    #             out_file.write(content)
    #             out_file.write("\n")
    #     out_file.write(self._close_tag())
    #     out_file.write("\n")

    def _open_tag(self):  # Returns the opening tag for the current element # Not Mine, 'Borrowed' from classmate
        return '<{}>'.format(self.tag)

    def _close_tag(self):  # Returns the closing tag for the current element # Not Mine, 'Borrowed' from classmate
        return '</{}>'.format(self.tag)


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
        out_file.write(self._open_tag())
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(self._close_tag())


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTab(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        tag = self._open_tag()[:-1] + " />\n"

        out_file.write(tag)


class Hr(SelfClosingTab):
    tag = 'hr'

    # def render(self, outfile):
    #     tag = "<{}".format(self.tag) + " />\n"
    #     outfile.write(tag)


class Br(SelfClosingTab):
    tag = 'br'

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
