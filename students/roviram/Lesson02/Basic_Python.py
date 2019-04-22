#-----------------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Desc: More Python Pushups Series Homework, Week 2
# Date Created: Sunday 4/21
# Python Pushups, List-1, has23
#-----------------------------------------------------------#
"""Given an int array length 2, return True if it contains a 2 or a 3.
has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""
def has23(nums):
    return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3


