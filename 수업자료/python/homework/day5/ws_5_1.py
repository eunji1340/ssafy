def reverse_string(input_string):
    result = []
    for i in reversed(input_string):
        result.append(i)
    return ''.join(result)
    
result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
