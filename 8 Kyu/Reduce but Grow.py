# Description:
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# My solution:

def grow(arr):
    product = 1
    
    for _ in arr:
        product = product * _
    
    return product
 
array = [1,2,3,4]
print(grow(array))
