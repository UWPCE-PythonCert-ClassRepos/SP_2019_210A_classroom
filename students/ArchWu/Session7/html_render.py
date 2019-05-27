#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element():

    tag = 'html'

    def __init__(self, content=None):
        self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        out_file.write("<html>")
        for content in self.contents:
            out_file.write(content)
        out_file.write("</html>")


class Body(Element):

    tag = 'body'

    def __init__(self, content=None):
        return super().__init__(content=content)

    def append(self, new_content):
        return super().append(new_content)
    
    def render(self, out_file):
        return super().render(out_file)