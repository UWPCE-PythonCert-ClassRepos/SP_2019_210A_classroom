#!/usr/bin/env python3


tag = 'html' # class object
indent = ''

# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)


    def append(self, new_content):
        self.content.append(new_content)


    def render(self, out_file):
        for content in self.content:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("/n")
            out_file.write("</{}>\n".format(self.tag))
