# 아래 함수를 수정하시오.
def even_elements(input_list):
    result = []
    
    for n in input_list:
        if n % 2 == 1:
            input_list.pop(input_list.index(n))

    result.extend(input_list)
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
