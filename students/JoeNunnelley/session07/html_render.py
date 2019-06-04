#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
# This is the framework for the base class
class Element():
    """
    An element has the format
        <tag [attribute=value, attribute=value /]>[text</tag>]
        lead tags can have attributes
        lead tags can exist by themselves but must end in a /
        blocks that have text must have a closing tag of the form </tag>
        tag blocks can have x children and be nested to any depth
    """
    tag = 'html'
    write_doctype = False
    indent = '   '
    depth = 0


    def __init__(self, content=None):
        """
        Initialize the class variables
        """
        self.attributes = []
        self.text = []
        self.children = []
        self.append(content)

    def get(self):
        """
        Base function to get block as a string
        """
        pass

    def append(self, new_content):
        """
        Append content to an element.
        There are four methods of doing this:
        1.) Using a class that is derived from Element
        2.) Using a dictionary containing iterable entries for attributes, text and children
        3.) Using a string to set just the text value of the tag
        4.) Using an empty new_content to just create the object with no values
        """
        if new_content is not None and self.tag is not None:
            if isinstance(new_content, Element):
                if isinstance(new_content, A):
                    self.text.append(new_content.get())
                else:
                    new_content.depth = self.depth + 1
                    self.children.append(new_content)
            elif isinstance(new_content, dict):
                self.attributes.append(new_content['attributes'])
                self.text.append(new_content['text'])
                self.children = new_content['children']
            elif isinstance(new_content, str):
                self.text.append(new_content)
            elif new_content is None:
                pass


    def render_children(self, children=None):
        """
        This function renders children that are not at the root of the document.
        """
        children_text = ''
        attribs = ''
        for child in children:
            if child.attributes and child.attributes[0]:
                attribs = ' ' + ''.join(child.attributes)

            start_tag = "\n{}<{}{}>".format((child.depth * child.indent), child.tag, attribs)
            tag_text = ''
            if child.text:
                tag_text = "\n{}{}".format(((child.depth + 1) * child.indent), ''.join(child.text))
            end_tag = "\n{}</{}>".format((child.depth * child.indent), child.tag)

            grandkids = child.render_children(child.children)
            child_text = "{}{}{}{}".format(start_tag, tag_text, grandkids, end_tag)
            children_text = children_text + ''.join(child_text)

        return children_text


    def render(self, out_file, ind=indent):
        """
        This function renders the root node and all descendants
        as well as writes the contents to the screen

        TODO : See about generalizing the render logic more so
        that it can handle all possible nodes.
        """
        self.indent = ind if self.indent != ind else self.indent

        attribs = ''
        if self.attributes and self.attributes[0]:
            attribs = ' ' + ''.join(self.attributes)

        start_tag = "{}<{}{}>".format((self.depth * self.indent), self.tag, attribs)
        tag_text = ''
        if self.text:
            tag_text = "\n{}{}".format(((self.depth + 1) * self.indent), ''.join(self.text))
        children_text = self.render_children(self.children)
        end_tag = "\n{}</{}>".format((self.depth * self.indent), self.tag)

        html_string = "{}{}{}{}".format(start_tag,
                                        tag_text,
                                        children_text,
                                        end_tag)
        if self.write_doctype:
            out_file.write('<DOCTYPE html>\n{}'.format(html_string))
        else:
            out_file.write(html_string)


class Html(Element):
    """
    The Html class derived from Element. This is the top of the document
    """
    tag = 'html'
    depth = 0
    write_doctype = True
    def __init__(self, content=None):
        super().__init__(content)


class Body(Element):
    """
    The Body class which derives from Element directly due to some testing requirments
    """
    tag = 'body'
    depth = Html.depth + 1
    def __init__(self, content=None):
        super().__init__(content)


class Head(Element):
    """
    The Head class which derives from Element directly due to some testing requirments
    """
    tag = 'head'
    depth = Html.depth + 1
    def __init__(self, content=None):
        super().__init__(content)


class Title(Head):
    """
    The Title class which derives from Head because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'title'
    depth = Head.depth + 1
    def __init__(self, content=None):
        super().__init__(content)


class Meta(Head):
    """
    The Meta class which derives from Head because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'meta'
    depth = Head.depth + 1
    def __init__(self, text='', charset='', children=[]):
        content = {"text":text, "attributes":'charset="{}"'.format(charset), "children":children}
        super().__init__(content)


class P(Body):
    """
    The P class which derives from Body because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'p'
    depth = Body.depth + 1
    def __init__(self, text, style=''):
        content = {"text":text, "attributes":style, "children":[]}
        super().__init__(content)


class Hr(Element):
    """
    The Hr class which derives from Element because it occurs anywhere
    """
    tag = 'hr'
    depth = Body.depth + 1
    def __init__(self, content=None):
        super().__init__(content)


class A(Body):
    """
    The A class which derives from Body because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'a'
    depth = Body.depth + 1
    def __init__(self, url, link):
        content = {"attributes":"href={}".format(url), "text":link, "children":[]}
        super().__init__(content)

    def get(self):
        return "<{} {}>{}</{}> ".format(self.tag,
                                        ''.join(self.attributes),
                                        ' '.join(self.text),
                                        self.tag)

class Li(Body):
    """
    The Li class which derives from Body because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'li'
    depth = Body.depth + 1
    def __init__(self, text="", style=''):
        content = {"attributes":"style={}".format(style), "text":text, "children":[]}
        super().__init__(content)

class Ul(Body):
    """
    The Ul class which derives from Body because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'ul'
    depth = Body.depth + 1
    def __init__(self, id, style, children=[]):
        content = {"attributes":"id={} style={}".format(id, style),
                   "text":"", "children":children}
        super().__init__(content)

class H(Body):
    """
    The H class which derives from Body because it only occurs there
    and we can therefore set a defacto dept based on it
    """
    tag = 'h'
    depth = Body.depth + 1
    def __init__(self, size, content):
        self.tag = self.tag + str(size)
        super().__init__(content)
