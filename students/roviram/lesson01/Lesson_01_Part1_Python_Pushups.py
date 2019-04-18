#---Dev Script---#
# Dev: Miguel Rovira-Gonzalez
# Script Creation Date: Monday 4/15/19
# Description: Lesson 1 Part 1 Python Pushups
# Warmup-1 > sleep_in Answer

#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
