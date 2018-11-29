# Authored by Patrick McNally
# Created on 09/15/15
# Requests a string and prints it reversed


def reverse_string(chars):
    """Takes in a string and returns it reversed.

    Parameters
    ----------
    Input:
    chars: string
    Any string or list 
    
    Output:
    chars: string
    A reversed version of the input
    """

    if chars:
        return chars[::-1]
    else:
        return None

def main():
    """Prompt user for a string and prints it reversed

    Parameters
    ----------
    Input:
    
    Output:
    """
    
    string_ = input("What string would you like reversed? ")
    rev_string = reverse_string(string_)
    print(rev_string)

assert reverse_string(None) == None
assert reverse_string(['']) == ['']
assert reverse_string(['f', 'o', 'o', ' ', 'b', 'a', 'r']) == ['r', 'a', 'b', ' ', 'o', 'o', 'f']


if __name__ == '__main__':
    main()