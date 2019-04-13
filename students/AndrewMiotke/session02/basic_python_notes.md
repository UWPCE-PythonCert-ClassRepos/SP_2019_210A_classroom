# Session 02: Basic Python - Notes

## Basic Value Types

### Numbers
* `float` = `3.14`
* `int` = `3125`

### Text
* `str` = `"Hello, this is a string with double quotes."` `'Hello, this is a string with single quotes.'`
	* double and single quotes work for strings, make sure to be consistant with which type of quotes are being used

### Boolean
Booleans or bools can only be `True` or `False`

* `True`
* `False`

### The nothing object
No value object, similar to null or nil 
* `None`

### Comments
Python comments start with a `#`
* `# here is a comment`

### Expressions
Evaluation an expression results in a value
* input: `3 + 4`
	* output: `7`

### Symbols
Must begin with an underscore or a letter
* `this_is_a_symbol` `_this_is_also_a_symbol`
* Symbols do not have a type

### Assignment
a _symbol_ is bound to a _value_ with the assignment operator, `=`

### Other Notes
* Python uses white space to delineate structure, meaning that white space matters.
* Python standard is 4 spaces for indentation
* Tabs are *not* Spaces and Spaces are *not* tabs
* `TypeErrors` are only checked at run time

### Functions
* Define a function using `def`
	* `def` is a statement
* Create a basic function like this:
```python
def simple():
	print("a simple function")
```
* To call a function, state the name and add `()` to the end of the function name.
	* To call the simple function about use `simple()`
* Calling a function is how you run the code in that function
* *Function Call Stack* is when a function calls another function.
	* This is often what a _trace back_ often refers to in exceptions
* Trace backs are listed in reverse order

### Functions `return`
* Every function ends by returning a value
```python
# the simplest possible function
def simple_return():
	return None
```
* If you don't put a `return` at the end, Python will return `None`
* Only one `return` will be run per function
* Any code after `return` will never be ran
```python3
def no_error():
	return `done`
	# no more will happen - the `return` ends the function
	print("this wont run")
```
* Functions _can_ return multiple results

### Function Parameters

