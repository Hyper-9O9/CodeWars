# Description
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]



# My solution:

def move_zeros(lst):
    new_lst = []
    zero = 0
    for item in range(len(lst)):
        if lst[item] != 0:
            new_lst.append(lst[item])
        else:
            zero += 1
            
    for _ in range(zero):
        new_lst.append(0)
                
    
    
    return new_lst
array = [1,0,1,2,0,1,3]
print(move_zeros(array))




# Best practice solution:
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

###############################

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
