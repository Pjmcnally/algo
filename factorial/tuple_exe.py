def tuple_full():
    count_dict = {}
    filename = input("input filename "  )
    file = open(filename, 'r')

    for line in file:
        lst = line.split(" ")
        if lst[0] == "From":
            

            if lst[1] in count_dict:
                count_dict[lst[1]] += 1
            else:
    	        count_dict.update({lst[1]: 1})
    print(count_dict)	    
        

tuple_full()
