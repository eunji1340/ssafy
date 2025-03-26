def ordered_difference_sets(set1, set2):
    result1 = set1 - set2
    result2 = set2 - set1

    if len(result1) <= len(result2):
        return result1, result2
    else:
        return result2, result1

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
