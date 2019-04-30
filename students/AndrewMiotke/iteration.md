# Iteration

### For Loops
```python3
In [13]: for x in "here's a string":
    ...:     print(x)
    ...:
s
t
r
i
n
g
```
* Unlike other languages, Python doesn't need an index to iterate through an array

### `range` and `for` Loops
* The `range` builtin is useful for looping a known number of times
```python3
In [15]: for i in range(5):
    ...:     print(i)
    ...:
0
1
2
3
4
```
* You don't need `i`, you could use a "nothing" name
```python3
In [16]: for _ in range(5):
    ...:     print("*")
    ...:
*
*
*
*
*
```
* Loops do not create a local namespace

### Loop Control
* Sometimes you want to interrupt or alter the flow of control through a loop
* Use `break` or `continue` to change or interrupt the flow
```python3
# break causes the loop to immediately end
In [17]: for i in range(101):
    ...:     print(i)
    ...:     if i > 50:
    ...:         break # the loop ends at 51
    ...:
```
```python3
# continue will skip the later statement in the loop and continue:
In [18]: for i in range(101):
    ...:     if i > 50:
    ...:         break
    ...:     if i < 25:
    ...:         continue
    ...:     print(i, end=' ')
    ...:
25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
```
* For loops can also take an optional `else` block
* Executed only when the loop exits normally(not via `break`)
```python3
In [20]:  for x in range(10):
    ...:     if x == 11:
    ...:        break
    ...: else:
    ...:     print("finished")
    ...:
finished

In [21]: for y in range(10):
    ...:     if y == 5:
    ...:         print(y)
    ...:         break
    ...: else:
    ...:     print('finished')
    ...:
5
```

### While Loops
* While loops are not for iterating over a collection or sequence, they are used for repeating something an _unknown_ number times.
* `while` loops continue until the condition is no longer True
```python3
while a_condition:
	some_code
```

### `while` vs `for`
* `while` is more general than `for`
* `while` is more error prone
* Easy to make an infinate loop with `while`
* To terminate a `while` loop use `break`
```python3
In [26]: while True:
    ...:     i += 1
    ...:     if i > 5:
    ...:     	break
    ...:     print(i)
```
* Set a flag:
```python3
In [31]: import random
In [32]: keep_going = True
In [33]: while keep_going:
    ...:     num = random.choice(range(5))
    ...:     print(num)
    ...:     if num == 3:
    ...:         keep_going = False
    ...:
4
1
2
3
```
* Use a conditional
```python3
In [35]: while i < 10:
    ...:     i += random.choice(range(4))
    ...:     print(i)
```
* Loop through two iterables at once with `zip`
```python3
In [36]: l1 = [1, 2, 3, 4, 5]
In [38]: l2 = [6, 7, 8, 9, 10]
In [42]: for i, j in zip(l1, l2):
    ...:     print(f"i:{i}, j:{j}")
    ...:
i:1, j:6
i:2, j:7
i:3, j:8
i:4, j:9
i:5, j:10
```

