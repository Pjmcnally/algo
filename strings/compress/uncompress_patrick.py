def uncompress(str1):
    if not str1:
        return str1
    else:    
        value = ""
        uncompress_lst = []
        lst1 = list(str1)
        for x in lst1:
            count = 1
            try:
                x = int(x)
                while count < x:
                    count += 1
                    uncompress_lst.append(value)
            except:
                value = x
                uncompress_lst.append(x)
        uncompress_str = "".join(uncompress_lst)
        return uncompress_str


assert uncompress(None) == (None)
assert uncompress("") == ("")
assert uncompress("A4B3CCD") == ("AAAABBBCCD")
assert uncompress("A3BBCD4") == ("AAABBCDDDD")
assert uncompress("A3BABABAB4C5") == ("AAABABABABBBBCCCCC")
assert uncompress("Mississippi") == ("Mississippi")