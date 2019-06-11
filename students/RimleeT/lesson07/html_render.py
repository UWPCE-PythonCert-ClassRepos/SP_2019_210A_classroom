#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"
    intent = ""

    def __init__(self, content=None, **kwargs):
        self.contents = [content] if content is not None else []
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")        
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def _set_intent(self, ind="", ind_count=0):
        self.intent = ind_count * ind

    def render(self, out_file, ind="", ind_count=0):
        self._set_intent(ind, ind_count)

        # loop through the list of contents:
        out_file.write(self.intent)
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, ind, ind_count + 1)
            except AttributeError:
                out_file.write(self.intent + ind)
                out_file.write(content)
                out_file.write("\n")

        out_file.write(self.intent)
        out_file.write(self._close_tag())
        out_file.write("\n")

class OneLineTag(Element):

    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, ind="", ind_count=0):
        self._set_intent(ind, ind_count)

        # loop through the list of contents:
        out_file.write(self.intent)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write("\n")


class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")
    
    def render(self, out_file, ind="", ind_count=0):
        self._set_intent(ind, ind_count)
        # loop through the list of contents:
        tag = self.intent + self._open_tag()[:-1] + " />\n"
        out_file.write(tag)


class Html(Element):
    tag = "html"

    def render(self, out_file, ind="", ind_count=0):
        self._set_intent(ind, ind_count)
        # loop through the list of contents:
        out_file.write(self.intent + '<!DOCTYPE html>\n')
        super().render(out_file, ind, 0)

class Head(Element):
    tag = "head"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Title(OneLineTag):
    tag = "title"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content, **kwargs):
        kwargs['href']=link
        super().__init__(content=content, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        if content == None:
            raise TypeError("Header can not without content")
        self.tag = self.tag + str(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"
