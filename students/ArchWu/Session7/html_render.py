#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element():
    tag = 'html'

    def __init__(self, content=None):
        self.contents = []
        if content: self.contents.append(content)

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
        self.contents.append("<body>")
        self.contents.append(new_content)
        self.contents.append("</body>")
        
    def render(self, out_file):
        out_file.write("<body>")
        for content in self.contents:
            out_file.write(content)
        out_file.write("</body>")

class P(Element):

    tag = 'p'

    def __init__(self, content=None):
        return super().__init__(content=content)
    
    def append(self, new_content):
        self.contents.append("<p>")
        self.contents.append(new_content)
        self.contents.append("</p>")
    
    def render(self, out_file):
        return super().render(out_file)


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
    
