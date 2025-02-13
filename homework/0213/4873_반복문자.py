T = int(input())
for tc in range(1, T+1):
    string = list(input())
    n = len(string)

    i = 0
    while i < len(string)-1:
        if string[i] == string[i+1]:
            string.pop(i+1)
            string.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1

    print(f'#{tc} {len(string)}')

# 강사님 코드
# def delete_repetition(text):
#     found = False
#     idx = -1
#     for i in range(len(text) - 1):
#         if text[i] == text[i+1]:
#             found = True
#             idx = i
#             break
#     if found:
#         return delete_repetition(text[:idx]+text[idx+2:])
#     else:
#         return text