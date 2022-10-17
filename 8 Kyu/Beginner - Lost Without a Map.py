# Description:
# Given an array of integers, return a new array with each value doubled.

# For example:
# [1, 2, 3] --> [2, 4, 6]

# My solution

def maps(a):
    new_array = []
    
    for _ in a:
        new_array.append(_*2)
    return new_array



array = [1,2,3,4]

print(maps(array))
