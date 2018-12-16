#!/bin/python3

def main():
    grid_size = int(input().strip())
    grid = []
    for grid_i in range(grid_size):
        grid_temp = list(input().strip())
        grid.append(grid_temp)
        
    mark_cavities(grid)
    for line in grid:
        print("".join(line))
    
def mark_cavities(grid):
    change_list = []
    for g_index, line in enumerate(grid[1:-1]):
        for l_index, item in enumerate(line[1:-1]):
            if item > max([
                    grid[g_index][l_index + 1],
                    grid[g_index + 1][l_index],
                    grid[g_index + 1][l_index + 2],
                    grid[g_index + 2][l_index + 1]
                ]):
                grid[g_index + 1][l_index + 1] = "X"      
    
main()