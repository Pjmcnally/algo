def find_missing_letter(chars):
    for i, item in enumerate(chars[1:]):
        if ord(item) != ord(chars[i]) + 1:
            return chr(ord(item) - 1)


print(find_missing_letter(["a", "b", "c", "d", "f"]))
