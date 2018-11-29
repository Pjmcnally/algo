# Authored by Patrick McNally
# Created on 09/15/15
# Requests a number from the user and generates a list of all primes 
#   upto and including that number.

import datetime


def list_primes(n):
    """Return a list of all primes up to "n"(inclusive).

    Parameters
    ----------
    Input:
    n: int or float
    A number
    
    Output:
    prime_list: list
    A list including all numbers up to "n"(inclusive)
    """

    prime_list = []
    for num in range(2, int(n) + 1):
        for div in range(2, int(num**.5 + 1)): 
            if num % div == 0: 
                break
        else:
            prime_list.append(num)
    return prime_list

def list_primes_better(n):
    """Return a list of all primes up to "n"(inclusive).

    Parameters
    ----------
    Input:
    n: int or float
    A number
    
    Output:
    prime_list: list
    A list including all numbers up to "n"(inclusive)
    """

   
    prime_list = [2]
    for num in range(2, int(n) + 1):
        for x in prime_list: 
            if num % x == 0: 
                break
            elif x > num**.5:
                prime_list.append(num)
                break
                

        
    return prime_list



def main():
    """Requests a number from the user and returns a list of all primes 
    up to and including that number.

    Parameters
    ----------
    Input:

    Output:
    """
    total_num = 5000000
    start = datetime.datetime.now()
    final = list_primes(total_num)
    end = datetime.datetime.now()
    first_try = end - start
    print("\nPrime finder process took {} seconds.\n".format(datetime.timedelta.total_seconds(first_try)))

    start = datetime.datetime.now()
    final2 = list_primes_better(total_num)
    end = datetime.datetime.now()
    sec_try = end - start
    print("\nBetter Prime finder process took {} seconds.\n".format(datetime.timedelta.total_seconds(sec_try)))

    if final == final2:
        print("both lists match")
    else:
        print("The lists are not the same")

# assert list_primes(1) == []
# assert list_primes(2) == [2]
# assert list_primes(12) == [2, 3, 5, 7, 11]
# assert list_primes(12.9) == [2, 3, 5, 7, 11]


if __name__ == '__main__':
    main()