def front3(str):
  if len(str)<3:
    str1= str*3
  str1= (str[0:3]*3)
  print(str1)
front3("Java")
front3("Chocolate")
front3("abcabcabc")
front3("ab")
front3("a")