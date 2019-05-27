#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element: # Did we need the () in Python3+ ?

    tag = 'html'

    def __init__(self, content=None):
        self.contents = [content]
        print("contents is:", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):
        if self.contents:
            out_file.write(f'<{self.tag}>\n')

            for content in self.contents:
                out_file.write(content)
                out_file.write('\n')

            out_file.write(f'</{self.tag}>\n')


    def create_page(self):
        page = Element("Some content")
        page.append("some more conntent")

        with open("test.html", "w") as out_file:
            page.render(out_file)



class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


    def render(self, out_file):
        if self.contents:
            out_file.write(f'<{self.tag}>\n')

            for content in self.contents:
                out_file.write(content)
                out_file.write('\n')

            out_file.write(f'</{self.tag}>\n')

b = Body()
b.create_page()

class P(Element):
    tag = 'p'