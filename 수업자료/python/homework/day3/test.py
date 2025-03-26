# # 문제3
# a = [1, 5, 3]
# b = [4, 2, 6]
# print(list(map(lambda x : max(x), zip(a,b))))
# print(list(map(max, zip(a,b))))

# # 문제4
# words = ["apple", "banana", "cherry"]
# numbers = [3, 5, 7]
# print(list(map(lambda x : x[0]+str(x[1]), zip(words, numbers))))
# print(list(map(lambda word, num : word + str(num), words, numbers)))

# # 문제5
# numbers = [1, 2, 3, 4, 5, 6]
# print(list(filter(lambda x : x % 2 == 0, numbers)))
# print([x for x in numbers if x % 2 == 0])

# # 문제6
# a = [2, 4, 6]
# b = [1, 3, 5]
# print(list(map(lambda x : x[0]*x[1], zip(a,b))))
# print(list(map(lambda x, y : x * y, a, b)))

# # 문제 7
# strings = ["hello", "world", "python"]
# print(list(map(lambda x: len(x), strings)))
# print(list(map(len, strings)))

# # 문제 8
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# print(list(map(lambda x: f'{x[0]}: {x[1]}', zip(names, ages))))
# print(list(map(lambda name, age : f'{name}: {age}', names, ages)))

# 1
a = [3, 8, 6, 10, 15]
b = [5, 7, 12, 9, 20]
print(list(filter(lambda x: x%2==0 ,map(max, zip(a,b)))))

# 2
words = ["a", "bb", "ccc"]
numbers = [1, 2, 3]
print(list(map(lambda word, number: word*number, words, numbers)))

# 3
strings = ["apple", "banana", "cherry", "kiwi"]
print(list(filter(lambda string : len(string) % 2 == 1, strings)))

# 4
numbers = [1, 2, 3, 4]
squares = [1, 4, 9, 16]
print(list(map(lambda number, square : f'{number}^2={square}', numbers, squares)))

# 5
nested_list = [[1, 4], [3, 5], [6, 8], [9, 2]]
print(list(filter(lambda n : n[1]>5, nested_list)))

# 6 
a = [2, 5, 3]
b = [4, 1, 6]
print(list(lambda x : x[0]*x[1], (filter(lambda l : l[0]*l[1]>10, zip(a, b)))))