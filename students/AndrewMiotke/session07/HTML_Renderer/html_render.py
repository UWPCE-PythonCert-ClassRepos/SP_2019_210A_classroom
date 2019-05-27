#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element: # Did we need the () in Python3+ ?

    tag = 'html'


    def __init__(self, content=None, **kwargs):
        self.__dict__.update(kwargs) # might not need this right now
        if content:
            self.contents = [content]
        else:
            self.contents = []


    def append(self, new_content):
        if self.contents is None:
            self.contents = []
            self.contents.append(new_content)
        else:
            self.contents.append(new_content)

    # Chris's initial render method
    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))


    # my render method
    # def render(self, out_file):
    #     out_file.write(f'<{self.tag}>\n')

    #     for content in self.contents:
    #         try:
    #             content.render(out_file)
    #         except AttributeError:
    #             out_file.write(content)
    #         out_file.write('\n')

    #     out_file.write(f'</{self.tag}>\n')


    def create_page(self):
        page = Element("Some content")
        page.append("some more conntent")

        with open("test.html", "w") as out_file:
            page.render(out_file)


e = Element()
e.create_page()


class OneLineTag(Element):
    def render(self, out_file):
        open_tag = [f"<{self.tag}"]
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        # out_file.write(f"<{self.tag}>")
        out_file.write(self.contents[0])
        out_file.write(f"</{self.tag}>\n")


    def append(self, content):
        raise NotImplementedError



class Title(OneLineTag):
    tag = 'title'



class Html(Element):
    tag = 'html'



class Head(Element):
    tag = "head"



class Body(Element):
    tag = 'body'



class P(Element):
    tag = 'p'


