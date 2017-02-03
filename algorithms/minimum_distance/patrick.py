#!/bin/python3

def main():
    junk = int(input().strip())
    array = [int(x) for x in input().strip().split(' ')]
    print(min_dist(array))
    
def min_dist(array):
    min_dist = None
    index_dict = {}
    for index, num in enumerate(array):
        temp_index = index_dict.get(num)
        if temp_index == None:
            index_dict[num] = index
        else:
            temp_dist = index - temp_index
            try:
                if temp_dist < min_dist:
                    min_dist = temp_dist
            except:
                min_dist = temp_dist
    
    if min_dist:
        return min_dist
    else:
        return -1
    
main()