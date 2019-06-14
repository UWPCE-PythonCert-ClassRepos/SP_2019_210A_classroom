#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    
    tag = "html"


    def __init__(self,content='None',**kwargs):
        self.content = content
        self.attribute = kwargs


    def append(self, new_content):
        self.new_content = str(new_content)
        self.content = self.content + self.new_content
        return self.content

    def render(self, out_file,ind=0):
        self.ind = " " * ind
        for k,v in self.attribute:
            out_file.write("<"+self.tag+k+"="+v+">"+"\n")
        out_file.write(self.ind+self.content + "\n")
        out_file.write("<"+"/"+self.tag+">")



class Html(Element):

    tag = 'html'


class Body(Element):

    tag = 'body'

    def render(self, out_file,ind=4):
        self.ind = " " * ind
        for k,v in self.attribute:
            out_file.write(self.ind+"<"+self.tag+k+"="+v+">"+"\n")
        out_file.write(self.ind*2+self.content + "\n")
        out_file.write(self.ind+"<"+"/"+self.tag+">")

class P(Element):

    tag = 'p'

    def render(self, out_file,ind=8):
        self.ind = " " * ind
        out_file.write(self.ind+"<"+self.tag+">"+"\n")
        out_file.write(self.ind*2+self.content + "\n")
        out_file.write(self.ind+"<"+"/"+self.tag+">")

class OnelineTag(Element):

    def render(self, out_file,ind=0):
        super().render(out_file,ind=0)
        line = "<{}> {} {} </{}>".format(self.tag,self.ind,self.content,self.tag)
        out_file.write(line)

class Title(OnelineTag):
    
    tag = 'title'

class Head(OnelineTag):

    tag = "H"

    def __init__(self, level=1, *args, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)

class Hr(Element):

    tag = "ul"
    def render(self, out_file,ind=4):
        super().render(out_file,ind=4)
        out_file.write(self.ind+"<"+self.tag+">"+"\n")

class A(Element):

    tag = "a"

    def __init__(self,link,content):
        super().__init__(content)
        self.attribute = {"href":link}




class Ul(Element):

    tag = "ul"


class Li(Element):

    tag = "li"
  