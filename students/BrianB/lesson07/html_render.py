#!/usr/bin/env python3

"""
A class-based system for rendering html.

I followed the homework and utilized the tutorial for
as far I could with great difficulty following the instruct.
The class lecture, online videos nor online readings were
much help with this assignment. I was able to sort mid-way
through Step 4 before turning to an alt source for help
completing the program.  This is noted in methods I sourced
help with.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = ""

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []  # creates an empty list
        else:
            self.contents = [content]  # creates a list with contents
            self.attribute = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        tag = f"<{self.tag}>"
        return tag

    def _close_tag(self):
        return f"<{self.tag}>"

    def render(self, out_file, indent="", ind_count=0):
        # loop through the list of contents
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    """
    Framework for 'html' tag, inherits from Element.
    Overrides render method and tag class attribute.
    """
    tag = 'html'

    def render(self, out_file, indent="", ind_count=0):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        self.indent = indent
        out_file.write(f'<!DOCTYPE html>\n')
        super().render(out_file, indent)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Li(Element):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'li'


class Ul(Element):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'ul'

    def __init__(self, content=None, **kwargs):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        if content: raise TypeError

        self.contents = []
        self.attributes = kwargs


class OneLineTag(Element):

    def render(self, out_file):
        # loop through the list of contents
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class H(OneLineTag):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        try:
            int(level)
        except ValueError:
            raise ValueError

        self.tag = f'h{level}'
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    tag = "title"


class A(OneLineTag):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        if not (content and link): raise TypeError

        kwargs['href'] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    def __init__(self, content=None, **kwargs):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        if content: raise TypeError
        self.attributes = kwargs

    def append(self, new_content):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        raise NotImplementedError

    def render(self, out_file, indent="", ind_count=0):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f' />\n')


class Hr(SelfClosingTag):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'hr'


# <br /> is XHTML format
class Br(SelfClosingTag):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'br'

    def __init__(self, content=None, **kwargs):
        """
        I was unable to follow the instructions beyond
        mid-Step 4, this was borrowed from an alt source
        """
        if kwargs: raise TypeError

        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    """
    I was unable to follow the instructions beyond
    mid-Step 4, this was borrowed from an alt source
    """
    tag = 'meta'
