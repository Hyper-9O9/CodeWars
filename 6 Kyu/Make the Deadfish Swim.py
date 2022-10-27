# Description

# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]



# My solution

def parse(data):
    arr = []
    value = 0
    
    for command in data:
        if command == 'i':
            value += 1
        if command == 'd':
            value -= 1
        if command == 's':
            print(value)
            value = value ** 2
        if command == 'o':
            arr.append(value)
        
    return arr
    
print(parse("iiisdoo"))


# Best practices
def parse(data):
    value = 0
    res=[]
    for c in data:
        if c=="i": value+=1
        elif c=="d": value-=1
        elif c=="s": value*=value
        elif c=="o": res.append(value)
    return res
