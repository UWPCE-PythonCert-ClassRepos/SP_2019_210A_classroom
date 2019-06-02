# Student: Miguel Rovira-Gonzalez
"""
PLEASE NOTE: This is not my code, I did not learn anything from this assignment and it did not teach me about Classes and Inheritance
I got stuck on step 5.
This was extremely difficult for a beginner programmer.
"""


# This is the framework for the base class
class Element():
    """
    Framework for a basic element in HTML code.
    Class attributes:
    tag:     Tag used for rendering html contents.  Element class is set to html.
    indent:  The level of indentation for the current element.
    """
    tag = 'html'
    indent = ''

    def __init__(self, content=None, **kwargs):
        """
        __init__ method for Element class.
        :param content: Content that is to be added to the instance content and later rendered.
        :param kwargs:  Used for passing in tag attributes.
        Attributes:
        contents    The content that is to be rendered into HTML format.
        """
        self.attributes = kwargs
        self.contents = [content] if content else []

    def _open_tag(self):
        """ Returns the opening tag for the current element """
        return f'<{self.tag}>'

    def _close_tag(self):
        """ Returns the closing tag for the current element """
        return f'</{self.tag}>'

    def append(self, new_content):
        """
        Appends new_content to the instance attribute content
        :param new_content: String that is to be appended to the instance content.
        """
        self.contents.append(new_content)

    def render(self, out_file, indent="", ind_count=0):
        """
        Recursively renders the instance attribute content into HTML format code.
        :param out_file: Destination for rendered text.
        :param indent: The specified indentation level for elements.
        :param ind_count: How many times indent should be applied to the element.
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f'{self._open_tag()[-1:]}\n')

        for content in self.contents:
            if hasattr(content, 'render'):
                content.render(out_file, indent, ind_count + 1)
            else:
                out_file.write(f'{self.indent}{indent}{content}\n')

        out_file.write(f'{self.indent}{self._close_tag()}\n')


class Html(Element):
    """
    Framework for 'html' tag, inherits from Element.
    Overrides render method and tag class attribute.
    """
    tag = 'html'

    def render(self, out_file, indent="", ind_count=0):
        """
        Adds <!DOCTYPE html> tag to output then calls super().render after running
        :param out_file: Destination for rendered text.
        :param indent: The specified indentation level for elements.
        :param ind_count: How many times indent should be applied to the element.
        """
        self.indent = indent
        out_file.write(f'<!DOCTYPE html>\n')
        super().render(out_file, indent)


class Body(Element):
    """
    Framework for 'body' tag, inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'body'


class P(Element):
    """
    Framework for 'p' paragraph tag, inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'p'


class Head(Element):
    """
    Framework for 'head' tag, inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'head'


class Li(Element):
    """
    Framework for 'li' list item tag, inherits from Element.
    Overrides tag class attribute.
    """
    tag = 'li'


class Ul(Element):
    """
    Framework for 'ul' unordered list tag, inherits from Element.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'ul'

    def __init__(self, content=None, **kwargs):
        """
        __init__ method for Ul class.
        :param content: Accepts no content, raises TypeError if content is passed it.
        :param kwargs:  Used for passing in tag attributes.
        """
        if content: raise TypeError

        self.contents = []
        self.attributes = kwargs


class OneLineTag(Element):
    """
    Framework for elements that render on a single line, inherits from Element.
    Overrides append and render methods.
    """
    def append(self, new_content):
        """
        Raises NotImplementedError if called.
        Overrides Element.append.
        One line tags can not append.
        """
        raise NotImplementedError

    def render(self, out_file, indent="", ind_count=0):
        """
        render method of OneLineTag class.
        Renders tag and attributes on a single line
        Overrides Element.render
        :param out_file: Destination for rendered text.
        :param indent: The specified indentation level for elements.
        :param ind_count: How many times indent should be applied for the element.
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f'{self._open_tag()[-1:]}')
        out_file.write(f'{self.contents[0]}')
        out_file.write(f'{self._close_tag()}\n')


class H(OneLineTag):
    """
    Framework for 'h' header tag, inherits from OneLineTag.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        """
        __init__ method for 'H' header class.
        Calls super().__init__ after execution
        :param content: Content that is to be added to the instance content and rendered.
        :param kwargs:  Used for passing in tag attributes.
        """

        # Verifies function called with interger value for header level as first parameter.
        # If it was forgotten, then contents will likely be the first passed value.
        # This 'should' then fail if casted to an int, and raises a ValueError
        try:
            int(level)
        except ValueError:
            raise ValueError

        self.tag = f'h{level}'
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    """
    Framework for 'title' tag, inherits from OneLineTag.
    Overrides tag class attribute.
    """
    tag = 'title'


class A(OneLineTag):
    """
    Framework for 'a' anchor tag, inherits from OneLineTag.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        """
        __init__ method for 'a' anchor class.
        adds href and link to kwargs and calls super().__init__ after execution
        :param link:    Anchor link passed in.
        :param content: Text that is to be added to the link.
        :param kwargs:  Used for passing in tag attributes.
        """
        if not (content and link): raise TypeError

        kwargs['href'] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    """
    Framework for self closing tag elements.
    Inherits from Element.
    Overrides __init__, append, and render methods.
    """
    def __init__(self, content=None, **kwargs):
        """
        __init__ method for SelfClosingTag class.
        :param content: Accepts no content, raises TypeError if content is passed it.
        :param kwargs:  Used for passing in tag attributes.
        """
        if content: raise TypeError

        self.attributes = kwargs

    def append(self, new_content):
        """
        Overrides Element.append.
        Self closing tags can not append.
        Raises NotImplementedError if called.
        """
        raise NotImplementedError

    def render(self, out_file, indent="", ind_count=0):
        """
        render method for SelfClosingTag class.
        Renders tag and attributes on a single line
        Overrides Element.render
        :param out_file: destination for rendered text
        :param indent: the specified indentation level for elements
        :param ind_count: how many times indent should be applied for the element
        """
        self.indent = indent * ind_count

        out_file.write(f'{self.indent}{self._open_tag()[:-1]}')
        for key, value in self.attributes.items():
            out_file.write(f' {key}="{value}"')
        out_file.write(f' />\n')


class Hr(SelfClosingTag):
    """
    Framework for 'hr' horizontal rule tag, inherits from SelfClosingTag.
    Overrides tag class attribute.
    """
    tag = 'hr'


# <br /> is XHTML format
class Br(SelfClosingTag):
    """
    Framework for 'br' horizontal rule tag, inherits from SelfClosingTag.
    Overrides __init__ method and tag class attribute.
    """
    tag = 'br'

    def __init__(self, content=None, **kwargs):
        """
        __init__ method for Br class.
        Checks that no attributes were passed then calls super().__init__
        :param content: Content that is to be added to the instance content and later rendered.
        :param kwargs:  br elements accept no attributes.  Raises TypeError is passed in.
        """
        if kwargs: raise TypeError

        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    """
    Framework for 'meta' rule tag, inherits from SelfClosingTag.
    Overrides tag class attribute.
    """
    tag = 'meta'