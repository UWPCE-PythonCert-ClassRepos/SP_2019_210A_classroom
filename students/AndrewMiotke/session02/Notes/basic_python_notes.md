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
* When declaring a function the values written inside the `( )` are parameters

### Function Arguments
* When you call a function your pass values into the function parameters. Thos values are called arguments.

### if/elif/else
* `elif` is Python's ways of saying `else if`

### Lists
* A way to store a bunch of stuff in order. Similar to an `array`
* You can put any objet in a list
```python3
list_of_int = [1, 2, 3, 4, 5]
list_of_strings = ["This", "is", "a", "string"]
```

### `for` Loops
* When you need to iterate over something multiple times, generally an object
```python3
list_of_int = [1, 2, 3, 4, 5]

for item in list_of_int:
	print(item)
```

### `range()` for Loop
* Allows you to iterate over something a set number of times
```python3
for i in range(1, 11):
	print(i) # prints numbers from 1 to 10
```

### `assert`
* Allows you to assert on a piece of code to ensure it does what you want, this is a part of unit testing
```python3
def add(n1, n2):
	return n1, + n2

assert add(2, 2) == 4 # this assertion would return nothing
assert add(2, 2) == 5 # This returns the following assertion failure:
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-24-0a40601796bd> in <module>
----> 1 assert add(2, 2) == 3

AssertionError:
```

