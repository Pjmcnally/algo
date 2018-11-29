#!/bin/python3

import sys


def main():
    org_string = input().strip()
    des_string = input().strip()
    tries = int(input().strip())
    
    if secret(org_string, des_string, tries):
        print("Yes")
    else:
        print("No")


def get_common_length(str1, str2):
    results = 0
    
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            results += 1
        else:
            break
            
    return results
        

def secret(org, des, tries):
    org_len = len(org)
    des_len = len(des)    
    common_length = get_common_length(org, des)
    opps_required = org_len + des_len - 2 * common_length

    # If you have enough tries to completely delete and replace the original string
    if tries > org_len + des_len:
        return True
    # If the things that need to change are greater than the opperations to change them.
    elif opps_required > tries:  
        return False
    # If enough tries (from if above) and they are both odd or even you are good
    elif opps_required % 2 == tries % 2:
        return True   
    # In all other cases.
    else:
        return False

main()
