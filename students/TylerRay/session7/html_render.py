#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""



class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for just text
    This allows the Element classes to render either Element objects or
    plain text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)



# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):

#        self.attributes = kwargs
        self.content = []
        if content:
            # call the classes append method
            # so that it can do anything special it needs to do
            self.append(content)

    def append(self, new_content):
        ''' adds new content or element to this element '''

        if hasattr(content, 'render'):
            self.content.append(content)
        else:

    self.content.append(TextWrapper(str(content)))


    def make_tags(self):
        """
        create the tags
        -- in a separate method so different subclass's render methods can use it
        """
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)

        return open_tag, close_tag



    def render(self, out_file):
        # Loop through the list of contents:

        out_file.write("<{}>\n".format(self.tag))
        for item in self.content:
            try:
                item.render(out_file)
            except AttributeError:
                out_file.write(item)
            out_file.write("\n")
        out_file.write("</{}>".format(self.tag))


class Html(Element):

    tag = "html"


class Body(Element):

    tag = "body"


class P(Element):

    tag = "p"


class Head(Element):

    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        # loop through the list of contents:
        for item in self.content:
            out_file.write("<{}>".format(self.tag))
            try:
                item.render(out_file)
            except AttributeError:
                out_file.write(item)
            out_file.write(("</{}>\n".format(self.tag)))


class Title(OneLineTag):

    tag = "title"


class SelfClosingTag(Element):
    """
    Base class for tags that have no content
    """

    def append(self, *args, **kwargs):
        """
        self closing tags can't have content, so we raise an error if someone
        tries to add some.
        """
        raise TypeError("You can not add content to a self closing tag")

    def render(self, out_file, ind=""):
        # there is some repition here -- maybe factor that out?
        open_tag, _ = self.make_tags()
        # make it a self cloding tag by adding the /
        out_file.write(ind + open_tag.replace(">", " />"))


class Hr(SelfClosingTag):
    """
    Horizontal Rule
    """
    tag = "hr"


class Br(SelfClosingTag):
    """
    Line break
    """
    tag = "br"


class A(OneLineTag):
    """
    anchor element
    """
    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        super().__init__(*args, **kwargs)
        # this could also be direct:
        # Element.__init__(self, *args, **kwargs)


class Ul(Element):
    """
    unordered list
    """
    tag = "ul"


class Li(Element):
    """
    list element
    """
    tag = "li"


class H(OneLineTag):
    """
    section head
    """
    tag = "H"

    def __init__(self, level, *args, **kwargs):
        self.tag = "h" + str(int(level))
super().__init__(*args, **kwargs)"