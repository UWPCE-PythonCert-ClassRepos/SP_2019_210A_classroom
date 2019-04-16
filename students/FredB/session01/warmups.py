#Warmups
#FredBallyns


def diff21(n):
#Returns absolute differnce with 21, but double if over 21
  if n <= 21:
    return 21-n
  else:
    return 2*(n-21)


def sleep_in(weekday, vacation):
#Returns true if not weekday or vacation
  return(not weekday or vacation)


def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return (a * b < 0)

