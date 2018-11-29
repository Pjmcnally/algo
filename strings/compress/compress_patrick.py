# Authored by Patrick McNally
# Created on 09/23/15
# Requests a string from the user and generates compressed version of 
#    the string.


def group_chars(str1):
    """Return a list of strings containing identical characters.

    Takes a string and iterates through it.  Each set of consecutive 
    identical characters are put in their own list entry.
    
    Parameters
    ---------
    Input:
    str1: String
    A string of characters to be compressed
    
    Output:
    letter_groupes: list
    A list of strings grouped by characters.
    """

    i = -1
    char = None
    letter_groups = []
    for x in str1:
        if x == char:
            letter_groups[i] += x
        else:
            letter_groups.append(x)
            char = x
            i += 1
    return letter_groups


def compress_groups(lst1):
    """Return a string containing compressed groups.

    Take a list of grouped strings and, if the string is 3 or longer compresses
    it down.  Each string is then appended to the final string.

    Parameters
    ---------
    Input:
    str1: List
    A list of strings grouped by characters.
    
    Output:
    out_string: String
    A compressed string containing letters and numbers.
    """    

    out_string = ""
    for x in lst1:
        if len(x) < 3:
            out_string += x
        else:
            out_string += x[0]
            out_string += str(len(x))
    return out_string


def compress(str1):
    """Return a compressed version of a string.
    
    Compresses the string by changing groups of 3 consecutive characters 
    or more in to a single character and a count. 
    
    Ex.
    --
    compress('AAABBCDDD')--> 'A3BBCD3'.
    
    The resulting string will always be shorter or the original string
    will be returned.

    Ex.
    --
    compress('A')--> 'A' # not 'A1'.

    Parameters
    ----------
    Input:
    string: 

    Output:
    """
    
    if not str1:
        return str1
    else: 
        lst1 = group_chars(str1)
        return compress_groups(lst1)


if __name__ == '__main__':
    str1 = input("Please enter the string you want to compress: ")
    print(compress(str1))


assert group_chars("AAAABBBCCD") == ["AAAA", "BBB", "CC", "D"]
assert compress_groups(["AAAA", "BBB", "CC", "D"]) == "A4B3CCD"
assert compress(None) == (None)
assert compress("") == ("")
assert compress("AAAABBBCCD") == ("A4B3CCD")
assert compress("AAABBCDDDD") == ("A3BBCD4") 
assert compress("AAABABABABBBBCCCCC") == ("A3BABABAB4C5")
assert compress("Mississippi") == ("Mississippi")





