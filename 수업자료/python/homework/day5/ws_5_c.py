def restructure_word(word, arr):
    for w in word:
        if w.isdecimal() == True:
            for _ in range(int(w)):
                arr.pop()
        else:
            arr.remove(w)

    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(list(original_word))
print(arr)

result = restructure_word(word, arr)
print(result)
result = ''.join(result)
print(result)