#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None):
        self.content_lst = [f"<{self.tag}>",]
        if content:
            self.content_lst.append(content)

    def append(self, *new_content):
        for item in new_content:
            self.content_lst.append(item)
        

    def render(self, out_file):
        for line in self.content_lst:
            try:
                line.render(out_file)
            except AttributeError:
                out_file.write(f"{line}\n")
        out_file.write(f"</{self.tag}>\n")
            
class Body(Element):
    tag = "body"

class Html(Element):
    tag = "html"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        for line in self.content_lst:
            try:
                line.render(out_file)
            except AttributeError:
                out_file.write(f"{line}")
        out_file.write(f"</{self.tag}>")

class Title(OneLineTag):
    tag = "title"
