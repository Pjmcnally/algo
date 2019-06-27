def next_smaller(n):
    dig_list = list(str(n))

    i = len(dig_list) - 2
    while i >= 0:
        # Look for possible swap. If the left digit is bigger than the right digit there is a valid swap.
        if dig_list[i] > dig_list[i + 1]:
            # Find best possible swap (biggest digit smaller than current digit), swap, reorder remaining digits and return.
            swap_group = dig_list[i:]
            next_small = max(x for x in swap_group if x < dig_list[i])
            # Check for invalid swap of 0 to front of number
            if i == 0 and next_small == "0":
                return -1
            swap_group.remove(next_small)
            dig_list[i:] = [next_small] + sorted(swap_group, reverse=True)
            return int("".join(dig_list))

        i -= 1

    return -1


print(next_smaller(1027))
