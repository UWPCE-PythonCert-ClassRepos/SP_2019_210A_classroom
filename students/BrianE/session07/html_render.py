#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out):
        file_out.write(self.text)


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def _build_attributes(self):
        attribute_strings = []
        for attribute in self.attributes:
            attribute_strings.append(f'{attribute}="{self.attributes[attribute]}"')
        return " ".join(attribute_strings)

    def render(self, out_file):
        if self.attributes:
            out_file.write(f'<{self.tag} {self._build_attributes()}>\n')
        else:
            out_file.write(f'<{self.tag}>\n')
        for content in self.content:
            if content:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
        out_file.write(f"</{self.tag}>\n")


class Html(Element):
    tag = 'html'

    def render(self, out_file, **kwargs):
        out_file.write(f'<!DOCTYPE html>\n')
        Element.render(self, out_file, **kwargs)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file):
        if self.attributes:
            out_file.write(f'<{self.tag} {self._build_attributes()}>')
        else:
            out_file.write(f"<{self.tag}>")
        for content in self.content:
            if content:
                if isinstance(content, str):
                    out_file.write(content)
                else:
                    content.render(out_file)
        out_file.write(f"</{self.tag}>\n")

    def append(self, content):
        raise NotImplementedError


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    def append(self, content):
        raise NotImplementedError

class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'

    def append(self, content):
        if isinstance(content, str):
            self.content.append(Li(content))
        elif isinstance(content, Li):
            self.content.append(content)


class Li(OneLineTag):
    tag = 'li'

    def append(self, content):
        if isinstance(content, str):
            self.content.append(TextWrapper(content))
        else:
            self.content.append(content)

class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def render(self, out_file):
        if self.attributes:
            out_file.write(f'<{self.tag} {self._build_attributes()} />\n')
        else:
            out_file.write(f'<{self.tag} />\n')


class Meta(SelfClosingTag):
    tag = "meta"


class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"
