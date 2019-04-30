# Python Sequences

### What is a Sequence? 
* Ordered collections of objects
* Sequences are also known as "arrays" or "lists" in other languages

### The Sequence Protocol
* A _sequence_ can be considered as anything that supports _at least_ these operations:
	* Indexing
	* Slicing
	* Membership
	* Concatenation
	* Length
	* Iteration

### Sequence Types
* There are eight built in types
	* string
	* list
	* tuple
	* bytes
	* bytearray
	* buffer
	* array.array
	* range object(almost)

### Indexing
* Items in a sequence can be looked up by their index using the index operator: `[ ]`
* Indexing always starts at `0`
```python3 
In [98]: s = "this is a string"
In [99]: s[0]
Out[99]: 't'
In [100]: s[5]
Out[100]: 'i'
```
* You can also use negative indexes to count from the end
```python3
In [2]: a_list = [34, 56, 19, 23, 55]

In [3]: a_list[-1]
Out[3]: 55

In [4]: a_list[-2]
Out[4]: 23

In [5]: a_list[-4]
Out[5]: 56
```
* Indexing beyound the end of the sequence causes an IndexError:
```python3
In [6]: a_list
Out[6]: [34, 56, 19, 23, 55]

In [7]: a_list[5]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-7-c1f9ac3b6fee> in <module>()
----> 1 a_list[5]

IndexError: list index out of range
```

### Slicing
* Slicing a sequence creates a new sequence with a range of objects for the original sequence
* Slicing uses the index operator(`[ ]`) but with a `:` in the middle
	* `sequence[start:finish]`
```python3
In [121]: s = "a bunch of words"
In [122]: s[2]
Out[122]: 'b'
In [123]: s[6]
Out[123]: 'h'
In [124]: s[2:6]
Out[124]: 'bunc'
In [125]: s[2:7]
Out[125]: 'bunch'
```
* You don't have to provide a start and finish for every slice
* You can leave off the start or finish value to lave off a certain part of a sequence
```python3
In [10]: s = 'this_could_is_a_filename.txt'

In [11]: s
Out[11]: 'this_could_is_a_filename.txt'

In [12]: s[:-4]
Out[12]: 'this_could_is_a_filename'

In [13]: s[-4:]
Out[13]: '.txt'
```
* Slicing can take a third argument: `step` which controls what items are returned
```python3
In [18]: a_tuple
Out[18]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

In [19]: a_tuple[0:15]
Out[19]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

In [20]: a_tuple[0:15:2]
Out[20]: (0, 2, 4, 6, 8, 10, 12, 14)
```

### Slicing vs Indexing
* Indexing will always return one single object(a scalar).
* Slicing will return a sequence of objects
* Indexing past the end of a sequence will raise the below error, slicing will not
```python3
In [129]: s = "a bunch of words"
In [130]: s[17]
----> 1 s[17]
IndexError: string index out of range
```

### Membership
* Sequences support `in` and `not in` membership operators
* Check to see if something is in a sequence
```python3
In [14]: s = [1, 2, 3, 4, 5]

In [15]: 5 in s
Out[15]: True

In [16]: 6 in s
Out[16]: False

In [17]: 2 not in s
Out[17]: False

In [18]: 23 not in s
Out[18]: True
```

### Concatenation
* Using `+` or `*` on sequence will _concatenate_ them
```python3
In [19]: l1 = [1, 2, 3, 4, 5]

In [20]: l2 = [6, 7, 8, 9, 10]

In [21]: l1 + l2
Out[21]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [22]: l1 * l2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-22-ec7519df584c> in <module>
----> 1 l1 * l2

TypeError: can't multiply sequence by non-int of type 'list'

In [23]: (l1 + l2) * 2
Out[23]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Length 
* Check the length of any sequence
```python3
In [26]: s = "these notes are very long."

In [27]: len(s)
Out[27]: 26
```

### Lists and Tuples
* Lists are constructed using `[ ]`, called list literals
```python3
# List literal
In [30]: []
Out[30]: []

In [31]: [1, 2, 3]
Out[31]: [1, 2, 3]

In [32]: [1, "jk", 7.23]
Out[32]: [1, 'jk', 7.23]
```
* Using `list` creates a list type object as a constructor
```python3
# Creates a list with the argument pass in
In [1]: list()
Out[1]: []

In [2]: list(range(4))
Out[2]: [0, 1, 2, 3]

In [3]: list('abcdefg')
Out[3]: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

### Tuples
* Tuples are constructing using tuple literals `( )`
```python3
In [4]: ()
Out[4]: ()

In [5]: (1, 2)
Out[5]: (1, 2)

In [6]: (1, 'a', 2.354)
Out[6]: (1, 'a', 2.354)
```
* Tuples don't need parentehses but they DO NEED commas
```python3
In [7]: t = 3, 3, 6, 9.23

In [8]: t
Out[8]: (3, 3, 6, 9.23)

In [9]: type(t)
Out[9]: tuple
```
* You can use the `tuple` type object to convert any iterable sequence into a tuple
```python3
In [11]: tuple(range(4))
Out[11]: (0, 1, 2, 3)

In [12]: tuple('Gus is a dog')
Out[12]: ('G', 'u', 's', ' ', 'i', 's', ' ', 'a', ' ', 'd', 'o', 'g')
```

### Mutability in Python
* All objects in Python are either `mutable` or `immutable`
* Immutable Types
	* String
	* Integer
	* Float
	* Tuple
* Mutable Types
	* List
	* Dictionary

### Choosing Lists or Tuples
* If it needs to be mutable: `list`
* If it needs to be immutable: `tuple`
	* provides safety when passing to a function(and as a key in `dict`(

* Do you need to do the same operation to each element?
	* `list`
* Is there a small collection of values which make a single logical item?
	* `tuple`
* Do you want to document that these values won’t change?
	* `tuple`
* Do you want to build it iteratively?
	* `tuple`
* Do you need to transform, filter, etc?
	* `list`
