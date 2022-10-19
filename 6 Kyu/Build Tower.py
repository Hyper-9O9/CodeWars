# Description:
# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# # My solution:

def tower_builder(n_floors):
    symbol = '*'
    pyramid = []
    for _ in range(n_floors):
        pyramid.append((((n_floors-1)-_)*" ")+(symbol*(_+_+1))+((n_floors-1)-_)*" ")
    
    return pyramid
    
print(tower_builder(3))


# Best practice:
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
