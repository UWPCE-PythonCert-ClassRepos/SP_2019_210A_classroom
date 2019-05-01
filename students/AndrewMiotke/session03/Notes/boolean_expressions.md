# Boolean Expressions

* Typically only `True` or `False` values. Boolean is a logical binary values 
* Booleans are often a data type
* Booleans are used `if` statements along with `and` and `or` operators

### Falsy
* `None`
* `False`
* Something that returns a zero value or an empty data type like a set or dictionary

### Truthy
* Everything that Falsy is not

### Pythonic Booleans
* This is redundant code because the `if` statement already checks if it's `True` or `False`
````python3
if xx == True:
	do_something()

# Even worse Python code
if bool(xx) == True:
	do_something()
```

* Below shows that the `if` statement already checks the boolean operation
```python3
if xx:
	do_something()
```

### `and`, `or`, and `not`
* Python has three boolean operators, `and`, `or`, and `not`
* `and` and `or` are binary expressions and evaluate from left to right
* `and` will return the first operand that evaluates to False, or the last operand if none are True.
```python3
In [6]: bool(0)
Out[6]: False

In [7]: bool(1)
Out[7]: True

In [8]: 0 and 1
Out[8]: 0
```
* `or` will return the first operand that evaluates to True, or the last operand if none are True
```python3
In [6]: bool(0)
Out[6]: False

In [7]: bool(1)
Out[7]: True

In [9]: 0 or 1
Out[9]: 1
```
* `not` is a unary expression(takes on operand) and inverts the boolean value of this operand. It just does the reverse
```python3
In [39]: not True
Out[39]: False

In [40]: not False
Out[40]: True
```

### Conditional Expersions
```python3
if something:
	x = a_value
else: 
	x = another_value
```

### Random Side Notes
```python3
In [1]: True == 1
Out[1]: True
In [2]: False == 0
Out[2]: True
```
* This is old legacy Python were bools are subclassed from integers(Int)
* This is _not_ recommended for modern Python
