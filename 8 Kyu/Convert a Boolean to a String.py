# Description

# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.




# My solution

def boolean_to_string(b):
    if b is True:
        return "True"
    else:
        return "False"
    
test = True

print(boolean_to_string(test))
