#!/bin/python3

def main():
    energy = 100
    num_clouds, jump_dist = (int(x) for x in input().strip().split(' '))
    clouds = [int(x) for x in input().strip().split(' ')]
    
    index = 0
    
    while energy >= 0:
        index = (index + jump_dist) % num_clouds
        energy -= (1 + clouds[index] * 2)
        
        if index == 0:
            return energy

    return "ran out of energy" #  Shouldn't happen 
        
print(main())
