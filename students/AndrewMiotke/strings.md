# Strings

* Strings are immutable

### Creating Strings
* String literal
```python3
string_with_double_quotes = "This string is valid with double quotes"
string_with_single_quotes = 'This string is valid with single quptes'
triple_double_quotes = """also valid"""
tripe_single_quotes = '''also
valid string code.
Creates multiple lines'''
```
* You can use `str()` to make a string out of other data types
```python3
In [43]: str(34)
Out[43]: '34'
```

### String Methods
* String methods are methods/functions that can be called on the string object
* `split` can split by searching for a particular charactor
```python3
# Using split
In [46]: csv = "comma, separated, values"

In [47]: csv.split(',')
Out[47]: ['comma', ' separated', ' values']
```
* `join` will join values with a particular charactor
```python3
# Using join
In [48]: psv = '|'.join(csv.split(','))
In [48]: psv = '|'.join(csv.split(','))

In [49]: psv
Out[49]: 'comma| separated| values'
```

### Case Switching
* There is a large range of methods that can be called on a string
```python3
In [50]: a_string = "A sentence that is a string"

In [51]: a_string.upper()
Out[51]: 'A SENTENCE THAT IS A STRING'

In [52]: a_string.lower()
Out[52]: 'a sentence that is a string'

In [53]: a_string.swapcase()
Out[53]: 'a SENTENCE THAT IS A STRING'

In [54]: a_string.title()
Out[54]: 'A Sentence That Is A String'
```
* You can test for certain classes of charactors
```python3
In [55]: number = "123456"
In [55]: number = "123456"

In [56]: number.isnumeric()
Out[56]: True

In [57]: number.isalnum()
Out[57]: True

In [58]: number.isalpha()
Out[58]: False

In [61]: fancy_string = "123kljklj$#%k"

In [62]: fancy_string.isalnum()
Out[62]: False
```

### String Literals
* You can use escape charactors such as `\n` to jump to the next line
* Common escape sequences
```python3
\\  Backslash (\)
\a  ASCII Bell (BEL)
\b  ASCII Backspace (BS)
\n  ASCII Linefeed (LF)
\r  ASCII Carriage Return (CR)
\t  ASCII Horizontal Tab (TAB)
\ooo  Character with octal value ooo
\xhh  Character with hex value hh
\uxxxx Charactor with Unicode code point value xxxx
\N{char-name} Charactor with Unicdoe name char_name
```
* Prints the string with a new line in the middle
```python3
In [78]: escape_char = "here is a \n new string."

In [79]: print(escape_char)
here is a
 new string.
 ```

### Raw Strings
* Raw strings allow you put a literal `\` in your string by putting a `r`before the quotes
```python3
In [80]: print("this\nthat")
this
that

In [81]: print(r"this\nthat")
this\nthat
```

### Ordinal Values
* Characters in strings are stored as numeric values(ASCII)
	* ASCII values: 1-127
* To get the value of a string use `ord()`
	* needs a `for` loop to iterate over the string _Gus_
```python3
In [84]: for i in "Gus":
    ...:     print(ord(i), end=' ')
    ...:
71 117 115
```
* To ge the characters from the unicode use `chr()`
```python3
In [87]: for i in (71, 117, 115):
    ...:     print(chr(i), end='')
    ...:
Gus
```
* For the English language, stick with ASCII, otherwise use, full Unicode: it’s easy with Python3

### Formatting Strings
* f-strings were introduced in Python 3.6, older version of Python do not support f-strings
* Use f-strings like so
```python3
In [88]: name = "Gus"

In [89]: print(f"My dog's name is {name}")
My dog's name is Gus
```
* You can  also format strings by using the `.format()` method but this seems more complicated
```python3
In [94]: "My dog's name is {}".format(dogs_name)
Out[94]: "My dog's name is Gus"
```
