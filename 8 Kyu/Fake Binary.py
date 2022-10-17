# Description:
#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

# My solution

def fake_bin(x):
    digits = ""
    for _ in x:
        if int(_) < 5:
            digits+='0'
        else:
            digits+='1'
    return digits

print(fake_bin('5521'))
