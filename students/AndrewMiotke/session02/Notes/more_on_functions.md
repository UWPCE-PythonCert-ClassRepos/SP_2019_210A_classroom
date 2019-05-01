# Session 02 - More on Functions: Notes

### Variable Scope
```python3
def fun(x, y):
	z = x + y
	return z
```
* `x`, `y`, `z` are local names
* `x` and `y` are parameter names
* `z` was bound inside the function

### Local vs Global
* Names or variables outside of a function are global
* If the name is a parameter it is local to that function
_global means it's only global to that module(typically the file) not global to the entire project or program._
* Best practice: Use global names for constants
* Best practice: Name constants using ALL_CAPS.
```python3
CONSTANT_NAME = ["fake", "data", "for", "constants"]
API_KEY = "some_fake_api_key_could_go_here"
```

### Parameters
```python3
def fun(x, y, z):
	print(x, y, z)
```
* The above parameters are alled _positional_ 
* You must provide arguements for all  _positional_ parameters in the same order of which they are listed
* You can provide default values for parameters in the function definition:
```python3
def fun(x=1, y=2, z=3):
	print(x, y, z)
```
* When parameters are given default values, those values become _optional_

### Recursion
* Recursion is when a function calls another function
* Python has a limit to how much recursion can happen to save system memory
```python3
def print_recursion(dogs_name):
	print(f"My dogs name is {dogs_name}, spelt with {len(dogs_name)} letters")
```
