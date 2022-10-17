# Description:
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


# My solution:

def digital_root(n):
    # we need a contain the sum in a variable
    sum = 0
    finished = False
    
    # while the statement is true repeat
    while not finished:
        # in order to find the length of the # we change it to string
        for _ in str(n):
        # we will add the numbers and store it in 'sum'
            sum += int(_)
        # we will equal n to sum, and set sum back to 0
        n = str(sum)
        sum = 0
        # if we are left with one digit, break the loop and return the integer
        if len(n) == 1:
            finished = True
    return int(n)
            
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))





# Best practice solutions:

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

# def digital_root(n):
#     return n%9 or n and 9 
