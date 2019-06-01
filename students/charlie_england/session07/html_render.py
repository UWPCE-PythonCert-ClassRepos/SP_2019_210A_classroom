#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None,**attributes):
        self.content_lst = [f"<{self.tag}>",]
        self.__dict__.update(attributes)
        if content:
            self.content_lst.append(content)
        if attributes:
            self.content_lst.pop(0)
            self.content_lst.insert(0,f'<{self.tag} ' +' '.join([f'{k}="{v}"' for k,v in attributes.items()]) + '>') #list comprehension to get a list of k:v pairs combined to be k='v', then joins these with spaces and attaches them to the tag line

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

    def render(self,out_file):
        out_file.write("<!DOCTYPE html>")
        Element.render(self,out_file)

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
        out_file.write(f"</{self.tag}>\n")

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None,**kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content,**kwargs)

    def render(self, out_file):
        if len(self.content_lst[0]) > 4:
            self.content_lst[0] = self.content_lst[0][:-1]
            out_file.write(self.content_lst[0] + " />\n")
        else:
            out_file.write(f"<{self.tag} />\n")
    
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"

    def __init__(self,link=None,content=None):
        self.content = content
        self.link = link
        super().__init__(content=content)

    def render(self, out_file):
        out_file.write(f'<{self.tag} href="{self.link}">{self.content}</{self.tag}>')

#Step 7:
class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    tag = "h"

    def __init__(self,level =1,content=None,**kwargs):
        self.tag = f"h{level}"
        super().__init__(content=content)
#Step 8:
class Meta(SelfClosingTag):
    tag = "meta"