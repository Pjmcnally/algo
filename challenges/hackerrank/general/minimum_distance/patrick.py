#!/bin/python3

def main():
    # Function to gather inputs and print output
    junk = int(input().strip())
    array = [int(x) for x in input().strip().split(' ')]
    print(min_dist(array))
    
def min_dist(array):
    # Min dist must be less than length of array.  Initialize here as impossible greater value.
    # Add 1 to protect check below "If min_dist == 1" from len 1 array
    array_len = len(array)
    min_dist = array_len
    
    # dictionary to hold value and last seen index
    index_dict = {}
    
    # Itterate over every index, elem in list.  
    for index, num in enumerate(array):
        temp_index = index_dict.get(num)
        # Check if value already seen
        if temp_index == None:
            # If not save to dict.
            index_dict[num] = index
        else: # if already seen compare new dist to min dist and replace or not.
            temp_dist = index - temp_index
            if temp_dist < min_dist:
                min_dist = temp_dist
        
        # 1 is the smallest possible dist.  No need to keep looking
        if min_dist == 1:
            break
    
    if min_dist == array_len:
        return -1
    else:
        return min_dist
    
main()