# Description:
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.



# My solution

def find_average(numbers):
    avg = 0
    if len(numbers) == 0:
        return 0
    for _ in numbers:
        avg += _
    return avg/len(numbers)
array = [1,2,3,4,5,6]
print(find_average(array))
