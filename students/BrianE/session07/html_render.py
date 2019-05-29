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


class Element(object):
    """
    Base class for rendering HTML elements
    """
    tag = 'html'
    indent = 0

    def __init__(self, content=None, **kwargs):
        self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def _build_attributes(self):
        """
        Generate attribute strings used within HTML tags

        :return: attribute strings
        """
        attribute_strings = []
        for attribute in self.attributes:
            attribute_strings.append(f'{attribute}="{self.attributes[attribute]}"')
        return " ".join(attribute_strings)

    def render(self, out_file, **kwargs):
        """
        Generate HTML tagging and write output to file

        :param out_file: HTML file
        :param kwargs: indentation arguments
        :return: None
        """
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.indent

        if self.attributes:
            out_file.write(f'{" " * indent}<{self.tag} {self._build_attributes()}>\n')
        else:
            out_file.write(f'{" " * indent}<{self.tag}>\n')

        for content in self.content:
            if content:
                try:
                    content.render(out_file, indent=indent + 4)
                except AttributeError:
                    out_file.write(f'{" " * indent}{" " * indent}{content}')
        out_file.write(f"{' ' * indent}</{self.tag}>\n")


class Html(Element):
    """ HTML class """
    tag = 'html'

    def render(self, out_file, **kwargs):
        """
        Similar to base class render(), but inserts DOCTYPE string

        :param out_file: HTML file
        :param kwargs: indentation arguments
        :return: None
        """

        out_file.write(f'<!DOCTYPE html>\n')
        Element.render(self, out_file, **kwargs)


class Body(Element):
    """ HTML body class """
    tag = 'body'


class P(Element):
    """ HTML paragraph class """
    tag = 'p'


class Head(Element):
    """ HTML head class """
    tag = 'head'


class OneLineTag(Element):
    """ Single-line HTML class """

    def render(self, out_file, **kwargs):
        """
        Similar to base class render() without newline after opening tag

        :param out_file: HTML file
        :param kwargs: indentation arguments
        :return: None
        """

        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.indent

        if self.attributes:
            out_file.write(f'{" " * indent}<{self.tag} {self._build_attributes()}>')
        else:
            out_file.write(f"{' ' * indent}<{self.tag}>")

        for content in self.content:
            if content:
                if isinstance(content, str):
                    out_file.write(f'{content}')
                else:
                    content.render(out_file)
        out_file.write(f"</{self.tag}>\n")

    def append(self, content):
        """ Sinle-line tags should not support multi-line content"""
        raise NotImplementedError


class A(OneLineTag):
    """ HTML anchor class """

    tag = 'a'

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    """ HTML header class """

    def __init__(self, level, content=None, **kwargs):
        self.tag = f"h{level}"
        super().__init__(content, **kwargs)


class Ul(Element):
    """ HTML unordered-list class """
    tag = 'ul'

    def append(self, content):
        if isinstance(content, str):
            self.content.append(Li(content))
        elif isinstance(content, Li):
            self.content.append(content)


class Li(OneLineTag):
    """ HTML list element class"""
    tag = 'li'

    def append(self, content):
        if isinstance(content, str):
            self.content.append(TextWrapper(content))
        else:
            self.content.append(content)


class Title(OneLineTag):
    """ HTML title class """
    tag = 'title'


class SelfClosingTag(Element):
    """ HTML self-closing tag class"""

    def render(self, out_file, **kwargs):
        """
        Similar to base class render() without newline after opening tag

        :param out_file: HTML file
        :param kwargs: indentation arguments
        :return: None
        """

        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.indent

        if self.attributes:
            out_file.write(f'{" " * indent}<{self.tag} {self._build_attributes()} />\n')
        else:
            out_file.write(f'{" " * indent}<{self.tag} />\n')


class Meta(SelfClosingTag):
    """ HTML meta class """
    tag = "meta"


class Hr(SelfClosingTag):
    """ HTML horizontal rule class """
    tag = "hr"


class Br(SelfClosingTag):
    """ HTML break class """
    tag = "br"
