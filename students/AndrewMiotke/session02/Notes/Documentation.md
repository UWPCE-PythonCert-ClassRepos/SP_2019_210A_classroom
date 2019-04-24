# Documentation

### Types of Documentation
* Comments
	* Common in all programming languages
* Docstrings
	* Less common and more unusual

### Comments
* Denoted inline with code
* In python, the `#` creates a comment for that line

### Docstrings
* Docstrings are used as inline documentation
* Can be used to document what a particular function or class does
```python3
def add_two_numbers(x, y):
"""Return the value of x + y"""
	return x + y
```

### Functional Docstrings Should:
* Be a complete sentence describing what the function does
	* `"""Return a list of values based on blah blah"""` is a good docstring
	* `"""Returns a list of values based on blah blah"""` is _not_ good
* Be useful on one line
	* If more description is needed, make the first line a complete sentence and add more lines below to elaborate
* Make sure a docstring is inclosed in three quotes `""" """`
