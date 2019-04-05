"""
Schedule students for lightning talks
"""
# needed to randomise the schedule
import random

# read the while file in as lines
students = open('students.txt').readlines()

# remove the header line
del students[0]

# strip the whitespace
students = [line.strip() for line in students]

# remove empty lines
students = [line for line in students if line]

# remove the languages, colon, etc.
students = [line.split(":")[0] for line in students]

# # reverse the first, last names
# # separate them:
# students = [line.split(",") for line in students]
# # put them back together
# students = ["{} {}".format(first.strip(), last) for last, first in students]

# put the list in random order
random.shuffle(students)

# make a list from 1 to 10
weeks = list(range(2, 11))

# make three of them...
weeks = weeks * 4

# put the students together with the weeks
schedule = zip(weeks, students)

# sort it for output
schedule = sorted(schedule)

# write it to a file (and print to screen)
with open('lightning_schedule.txt', 'w') as outfile:
    for week, student in schedule:
        line = 'week {}: {}\n'.format(week, student)

        print(line)
        outfile.write(line)
