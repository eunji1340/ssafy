def find_min_max(input_list):
    result = min(input_list), max(input_list)
    return result


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
