#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    indent = "    "
    def __init__(self, content=None, **attrs):
        self.content = []
        self.tag = "html"
        if content:
            self.content.append(content)
        self.attrs = {}
        if attrs:
            self.attrs = attrs

    def append(self, new_content):
        self.content.append(new_content)
        '''
        if isinstance(new_content, str):
            self.content += "\n"
            self.content += new_content
        elif isinstance(new_content, Element):
            self.objectContents.append(new_content)
        '''
    def render(self, out_file, indent=""):
        out_file.write(indent + self.genHeaderWithAttrs() + "\n")
        newLine = ""
        for c in self.content:
            if isinstance(c, str):
                out_file.write(indent + self.indent + c)
            else:
                c.render(out_file, indent + self.indent)
            out_file.write("\n")
        out_file.write(indent + "</" + self.tag + ">")

    def genHeaderWithAttrs(self):
        output = "<" + self.tag
        for key, val in self.attrs.items():
            output += " {0}=\"{1}\"".format(key, val)
        output += ">"
        return output


class Html(Element):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = "html"

    def render(self, out_file, indent=""):
        out_file.write(indent + "<!DOCTYPE html>\n")
        Element.render(self, out_file, indent)


class Body(Element):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = "body"


class P(Element):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = 'p'


class Head(Element):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = 'head'


class OneLineTag(Element):
    def render(self, out_file, indent=""):
        out_file.write(indent + self.genHeaderWithAttrs())
        for c in self.content:
            if isinstance(c, str):
                out_file.write(c)
        out_file.write("</" + self.tag + ">")


class Title(OneLineTag):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = 'title'


class SelfClosingTag(Element):
    def render(self, out_file, indent=""):
        headerWithAttr = self.genHeaderWithAttrs()
        headerWithAttr = headerWithAttr[:-1]
        headerWithAttr += "/>"
        out_file.write(indent + headerWithAttr)


class Hr(SelfClosingTag):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = 'hr'



class Br(SelfClosingTag):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = 'br'


class A(SelfClosingTag):
    def __init__(self, link, content=None, **attrs):
        Element.__init__(self, content, href="{}".format(link))
        self.tag = "a"


class Ul(Element):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = "ul"


class Li(Element):
    def __init__(self, content=None, **attrs):
        Element.__init__(self, content, **attrs)
        self.tag = "li"

class H(OneLineTag):
    def __init__(self, headersize, content=None, **attrs):
        OneLineTag.__init__(self, content, **attrs)
        self.tag = "h" + str(headersize)

class Meta(SelfClosingTag):
    def __init__(self, content=None, **attrs):
        SelfClosingTag.__init__(self, content, **attrs)
        self.tag = "meta"





