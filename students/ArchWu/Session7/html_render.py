#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    kwarg = {}
    def __init__(self, content=None, **kwargs):
        self.contents = []
        if content: self.contents.append(content)
        kwarg = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = 'html'

    def __init__(self, content=None):
        return super().__init__(content=content)

    def append(self, new_content):
        return super().append(new_content)
    
    def render(self, out_file):
        return super().render(out_file)
    

class Body(Element):

    tag = 'body'

    def __init__(self, content=None):
        return super().__init__(content=content)

    def append(self, new_content):
        return super().append(new_content)
    def render(self, out_file):
        return super().render(out_file)

class P(Element):

    tag = 'p'

    def __init__(self, content=None, **kwargs):
        return super().__init__(content=content, **kwargs)
    
    def append(self, new_content):
        return super().append(new_content)
    
    def render(self, out_file):
        for content in self.contents:
            out_file.write("<{}".format(self.tag))
            for k,v in self.kwarg:
                out_file.write("{}={}".format(k, v))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("/{}>".format(self.tag))


class Head(Element):
    tag = "head"

    def __init__(self, content=None):
        return super().__init__(content=content)
    
    def append(self, new_content):
        return super().append(new_content)
    
    def render(self, out_file):
        return super().render(out_file)
    
class OneLineTag(Element):

    def render(self, out_file):
        head = "<{}>".format(self.tag)
        for content in self.contents:
            head += content
        endings = "</{}>\n".format(self.tag)
        out_file.write(head + endings)
    
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'
    def __init__(self, content=None):
        return super().__init__(content=content)
    
    def render(self, out_file):
        return super().render(out_file)
    
