def remove_duplicates(input_list):
    new_lst = []
    #new_lst = list(set(input_list))
    for i in input_list:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)