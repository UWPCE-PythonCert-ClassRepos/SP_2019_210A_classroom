#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write("<{}>\n".format(self.tag))
        for line in self.content:
            out_file.write(line)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"



