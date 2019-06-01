"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io

# import * is often bad form, but makes it easier to test everything in a module.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
    return outfile.getvalue()


########
# Step 1
########

def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    element = Element()
    element = Element("this is some text")
    assert "this is some text" in element.text


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    element = Element("this is some text")
    element.append("some more text")
    assert "this is some text" in element.text
    assert "some more text" in element.text


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    element = Element("this is some text")
    element.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(element).strip()

    # making sure the content got in there.
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


# Uncomment this one after you get the one above to pass
# Does it pass right away?
def test_render_element2():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    element = Element()
    element.append("this is some text")
    element.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(element).strip()

    # making sure the content got in there.
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")


# ########
# # Step 2
# ########

# tests for the new tags
def test_html():
    """
    Test that the Html object is properly initialized
    """
    element = Html("this is some text")
    element.append("and this is some more text")

    file_contents = render_result(element).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    """
    Test that the body object is properly initialize
    """
    element = Body("this is some text")
    element.append("and this is some more text")

    file_contents = render_result(element).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    """
    Test the the P object is properly initialized
    """
    element = P("this is some text")
    element.append("and this is some more text")

    file_contents = render_result(element).strip()

    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents

########
# Step 3
########


def test_attribute_embedding():
    """
    Here we test dictionary method to initialize the elements of a tag
    """
    meta = Meta(text='boo', charset="UTF-8", children=[])
    assert meta.text[0] == 'boo'
    assert meta.attributes[0] == 'charset="UTF-8"'
    assert meta.children == []
    print(render_result(meta))


def test_class_embedding():
    """
    Here we test the initializing and appending the page with classes
    """
    meta = Meta(text='boo', charset="UTF-8", children=[])
    head = Head('This is the head')
    head.append(meta)
    assert isinstance(head.children[0], Meta)
    print(render_result(head))

    body = Body('This is the body')
    body.append(P('This is a comment'))
    assert isinstance(body.children[0], P)
    print(render_result(body))
    print()


def test_child_class_embedding():
    """
    Here we test the ability to initialize children using the dictionary init method
    """
    head = Head("This is the head")
    head.append(Meta(text='boo', charset="UTF-8", children=[]))
    head.append(Title("This is the title"))
    body = Body("This is the body")
    children = [head, body]
    page = Html({'text':'here is the html text',
                 'attributes': 'id=head_object',
                 'children':children})
    file_contents = render_result(page)
    print(file_contents)
    lines = file_contents.split('\n')
    assert lines[1] == '<html id=head_object>'
    assert lines[3] == '   <head>'
    assert lines[5] == '      <meta charset="UTF-8">'
    assert lines[8] == '      <title charset="UTF-8">'
    assert lines[11] == '   </head>'
    assert lines[12] == '   <body>'
    assert lines[-1] == '</html>'


# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer

    NOTE : I believe this test was in error. the HTML tag should indent 0 per the sample.html.
    I have updated the test to expect the sample.html format
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("<")  # DOCTYPE should be left aligned
    assert lines[1].startswith("<")  # html tag should be left aligned
    assert lines[2].startswith("   ")
    print(repr(lines[-1]))
    assert lines[-1].startswith("<")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    print("[{}]".format(lines))
    print(lines[1])
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * Element.indent + "<")

    assert lines[4].startswith(3 * Element.indent + "some")


def test_href_insertion():
    """
    Test the special case of inline A object insertion
    """
    item = Li()
    item.append("And this is a ")
    item.append(A("http://google.com", "link"))
    item.append("to google")
    file_contents = render_result(item)
    print(file_contents)


def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    <\\html> # had to escape the backslash here for pylint :)

    More complex indentation should be tested later.
    """
    element = Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(element).strip()
    print(file_contents)
    # making sure the content got in there.
    assert "this is some text" in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")
