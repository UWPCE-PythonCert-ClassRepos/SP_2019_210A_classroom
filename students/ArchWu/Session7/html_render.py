# #!/usr/bin/env python3

# """
# A class-based system for rendering html.
# """

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


class Element:

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = kwargs
        if content:
            # call the classes append method
            # so that it can do anything special it needs to do
            self.append(content)

    def append(self, content):
        """
        add a new piece of content or another element to this element
        """
        # note: this changed the internal represntation of content
        #       it no longer holds strings -- so a test will fail
        #       but that test was testing internal API --
        #       it's probably better remove it
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, out_file, ind=""):
        opentag, closetag = self.make_tags()
        out_file.write("{}{}\n".format(ind, opentag)) 
        for stuff in self.content:
            stuff.render(out_file, ind + self.indent)
            out_file.write("\n")
        out_file.write("{}{}".format(ind, closetag))

    def make_tags(self):
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)
        return open_tag, close_tag

class OneLineTag(Element):
    def render(self, out_file, ind=""):
        # there is some repition here -- maybe factor that out?
        opentag, closetag = self.make_tags()
        out_file.write("{}{}".format(ind, opentag))
        for stuff in self.content:
            stuff.render(out_file)
        out_file.write("{}{}".format(ind, closetag))
    
    # def append(self, content):
    #     raise NotImplementedError
    # this always breaks other tests when a non-oneliner object appends a one-liner object



class Html(Element):
    tag = 'html'
    def render(self, out_file, ind=''):
        out_file.write(ind + "<!DOCTYPE html>\n")
        super().render(out_file, ind = ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def append(self, *args, **kwargs):
        raise TypeError
    
    def render(self, out_file, ind=''):
        opentag, _ = self.make_tags()
        out_file.write("{}{}".format(ind, opentag.replace(">", " />")))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    """Link"""
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    """Unordered List"""
    tag = "ul"

class Li(Element):
    """List"""
    tag = "li"

class H(OneLineTag):
    """Head"""
    tag = 'h'

    def __init__(self, header, *args, **kwargs):
        self.tag = 'h' + str(int(header))
        super().__init__(*args, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'