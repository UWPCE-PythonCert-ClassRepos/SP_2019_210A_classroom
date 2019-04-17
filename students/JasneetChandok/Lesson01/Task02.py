'''
Lesson: 01
Task Number: 02 - CodingBat Python
Student Name: Jasneet Chandok
Last Update Date: 04/14/19
'''
#!/usr/bin/env python3.6

# Warmup -1 > sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)

# Warmup -1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

# Warmup -1 > sum_double
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum