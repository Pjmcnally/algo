def open_file():
    """Opens file and saves text as a variable"""
    filename = input("input filename "  )
    file = open(filename, 'r')
    return file

def clean_func(thing):
    list_out = []
    cruft = [".", "?", "!", "\n", ",", "~", ":", ";","(", ")",'"', "'s"]
    for line in thing:
        for elem in cruft:
            line = line.replace(elem, "")
        list_out.append(line.lower())
    return list_out

    
def count_letter_dict(thing):
    k = 'zxcvbnmpoiuytrewqasdfghjkl'
    dict_letter = {}
    for line in thing:
        for elem in line:
            if elem in k:
                if elem in dict_letter:
                    dict_letter[elem] += 1
                else:
                    dict_letter.update({elem : 1})
    return dict_letter

def count_word_dict(thing):
    dict_word = {}
    for line in thing:
        lower = line.split(" ")
        for elem in lower:
            if elem in dict_word:
                dict_word[elem] += 1
            else:
                dict_word.update({elem : 1})
    return dict_word
    
def listify(dict1):
    list_out = []
    for letter, count in dict1.items():
        list_out.append([count, letter])
    list_out.sort()
    return list_out
    
def main():
    iter1 = open_file()
    clean_list = clean_func(iter1)

    letter_dict = count_letter_dict(clean_list)
    word_dict = count_word_dict(clean_list)

    print_letter_list = listify(letter_dict)
    print_word_list = listify(word_dict)

    for elem in print_letter_list:
        print(elem)
    for elem in print_word_list:
        print(elem)
    
main()