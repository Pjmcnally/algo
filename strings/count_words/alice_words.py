def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file1 = open(filename, 'r')
    return file1

def clean_func(thing):
    list_out = []
    cruft = [".", "?", "!", "\n", ",", "~", ":", ";","(", ")",'"', "'s", "_", "-", "&", "*", "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "wwwgutenbergorg", "[illustration]"]
    for l in thing:
        line = l.rstrip()
        if line:
            for elem in cruft:
                line = line.replace(elem, "")
            list_out.append(line.lower())
    return list_out

def count_word_dict(thing):
    dict_word = {}
    for line in thing:
        for elem in line.split(" "):
            dict_word[elem] = dict_word.get(elem, 0) + 1
    return dict_word

def main():
    stuff = open_file()
    list_out = clean_func(stuff)
    dict_word = count_word_dict(list_out)
    for elem in sorted(dict_word.items(), key=lambda x:x[1]):
        print(elem)

main()

