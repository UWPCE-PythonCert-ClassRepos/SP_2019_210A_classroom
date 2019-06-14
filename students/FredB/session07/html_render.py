#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""



class Element:
#class attribute
    tag = "html"
    indent = "    "
    newline = 1

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = [] #Initialize as list
        if content:
         self.append(content)

    def append(self, new_content):
        self.content.append(new_content)

    def toggle(self,txt):
        if self.newline == 1:
            return txt
        return ""

    def make_tags(self):
        if self.attributes:
            for key, value in self.attributes.items():
                attri = (" {}=\"{}\"".format(key, value))
        else:
            attri=""
        open_tag = "<"+self.tag+attri+">"
        close_tag = "</"+self.tag+">"
        return open_tag, close_tag

    def render(self, out_file, current_indent=""):
        open_tag, close_tag = self.make_tags()
        out_file.write(current_indent+open_tag+self.toggle("\n"))
        for elem in self.content:
            if type(elem) == str:
                out_file.write(self.toggle(current_indent+self.indent)+elem+self.toggle("\n"))
            else:
                elem.render(out_file, current_indent + self.indent)
        out_file.write(self.toggle(current_indent)+close_tag+"\n")


class Html(Element):
    #class attribute restate
    tag = 'html'
    def render(self, file_out, current_indent=""):
        file_out.write(current_indent + "<!DOCTYPE html>\n")
        super().render(file_out, current_indent=current_indent)


class Body(Element):
    #class attribute override
    tag = "body"


class P(Element):
    #class attribute override
    tag = "p"

class Head(Element):
    tag = "head"

class Ul(Element):
    #unordered list
    tag = "ul"

class Li(Element):
    #list element
    tag = "li"




class OneLineTag(Element):
    newline = 0

class Title(OneLineTag):
    tag = "title"

class A(OneLineTag):
    #anchor element
    tag = "a"

    def __init__(self, link, content,**kwargs):
        kwargs['href'] = link
        super().__init__(content=content, **kwargs)

class H(OneLineTag):
    #section head
    tag = "H"

    def __init__(self, level, content, **kwargs):
        if type(level) == str:
            level.strip()
        try:
            val = int(level)
        except ValueError:
            print("Level must be a number")
        self.tag = "h" + str(val)
        super().__init__(content=content, **kwargs)




class SelfClosingTag(Element):

    def append(self, *args, **kwargs):
        #raise error as cant have content
        raise TypeError("Error: self closing tags can’t have any content")

    def render(self, out_file, current_indent=""):
        open_tag, _ = self.make_tags()
        # add indent and switch the ending
        out_file.write(current_indent + open_tag[:-1]+" />\n")

class Hr(SelfClosingTag):
    #horizontal rule
    tag = "hr"

class Br(SelfClosingTag):
    #line break
    tag = "br"

class Meta(SelfClosingTag):
    #metadata tag
    tag = "meta"
