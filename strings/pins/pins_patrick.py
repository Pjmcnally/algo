# Authored by Patrick McNally
# Created on 09/25/15
# Requests a number from the user and returns a pronouncable string 
#   representing the number input.


def break_string(num):
    """Return a list of numbers broken into two digit pieces.

    Take a number and iterates through it.  Each two digit chuch of the
    digit are broken off and attacked to a list.  The list is then reversed 
    to match the original order. 
    
    Parameters
    ---------
    Input:
    num: Int
    A number to be converted to a pronouncable string.
    
    Output:
    new_lst: List
    A list of the number broken into pieces of 2 digits or smaller.
    """

    new_lst = []
    while num:
        new_lst.append(num % 100)
        num = int(num // 100)
    new_lst.reverse()
    return new_lst

def num_to_char(lst_):
    """Return a pronouncable string from a list of numbers. 

    Each two digit chunk in the list is converted to a pronouncable string
    of two characters.  This is then appended to the final string to be 
    returned to the user.
    
    Parameters
    ---------
    Input:
    lst_: List 
    A list of numbers 2 digits or less
    
    Output:
    new_str: String
    A pronouncable string representing the original number entered.
    """

    CONSONANTS = "bcdfghjklmnpqrstvwyz"
    VOWELS = "aeiou"  
    new_str = ""
    for x in lst_:
        new_str += CONSONANTS[x // 5]
        new_str += VOWELS[x % 5]
    return new_str

def convert_pin(num):
    """ Return a pronouncable string from any number

    The core of this program is the idea that any two digit number (100 
    total) can be converted to a combination of 1 consonant (not including 
    x or y) and 1 vowel (not including y) (100 total).

    Parameters
    ---------
    Input:
    num: Int
    A number to be converted to a pronouncable string.
    
    Output:
    out_str: String
    A pronouncable string representing the original number entered.
    """


    try:
        if num <= 0:
            return ValueError
        new_lst = break_string(num)
        out_str = num_to_char(new_lst)
        return out_str
    except:
        return ValueError



assert break_string(4327) == [43, 27]
assert break_string(1298) == [12, 98]
assert break_string(54327) == [5, 43, 27]
assert num_to_char([43, 27]) == "lohi"
assert num_to_char([12, 98]) == "dizo"
assert num_to_char([5, 43, 27]) == "calohi"

assert convert_pin(None) == ValueError
assert convert_pin('absd')== ValueError
assert convert_pin(0) == ValueError
assert convert_pin(4327) == "lohi"
assert convert_pin(1298) == "dizo"


if __name__ == '__main__':
    num = eval(input("What number would you like to make pronouncable? "))
    print("The pronouncable version of your number is :", convert_pin(num))


