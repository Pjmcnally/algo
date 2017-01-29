def main():
    """ Main func to group core logic """
    tests = int(input().strip())
    
    for x in range(tests):
        array = [x for x in input().strip()]
        print(display_as_str(permute(array)))
        
def permute(array):
    # setup basic variables
    arr_len = len(array)
    i = arr_len - 1
    pivot = None
    
    # find longest non-increasing suffix
    while i > 0:
        if array[i] > array[i - 1]:
            pivot = i - 1
            break
        i -= 1
        
    # if pivot exists switch pivot with lowest value in suffix higher than pivot
    if pivot == None:
        return None
    else:
        j = arr_len - 1
        while j >= 0:
            if array[j] > array[pivot]:
                switch(array, j, pivot)
                break
            j -= 1
            
    # reverse suffix 
    array[pivot + 1:] = reversed(array[pivot + 1:])
    return array


def switch(array, i, j):
    """Function to take in array and 2 index.  Switch values at index (in place) and return array"""
    array[i], array[j] = array[j], array[i]
    return array


def display_as_str(array):
    """Function to conver array to string (even if it contains ints)"""
    if array:
        return "".join(str(x) for x in array)
    else:
        return "no answer"

main()