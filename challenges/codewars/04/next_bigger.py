def next_bigger(n):
    dig_list = list(str(n))

    i = len(dig_list) - 2
    while i >= 0:
        # Look for possible swap. If the left digit is smaller than the right digit there is a valid swap.
        if dig_list[i] < dig_list[i + 1]:
            # Find best possible swap (smallest digit bigger than current digit), swap, reorder remaining digits and return.
            swap_group = dig_list[i:]
            next_big = min(x for x in swap_group if x > dig_list[i])
            swap_group.remove(next_big)
            dig_list[i:] = [next_big] + sorted(swap_group)
            return int("".join(dig_list))

        i -= 1

    return -1


print(next_bigger(787763292932))
