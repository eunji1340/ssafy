laser = input()
n = len(laser)
ct = 0
stack = []

for i in range(n):
    if laser[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if laser[i-1] == '(':
            ct += len(stack)
        else:
            ct += 1

print(ct)
# i = 1
# while i < n:
#     if laser[i-1] == '(' and laser[i] == ')':
#         laser[i-1], laser[i] = "0", "1"
#     i += 1
#
# ct = 0
# end = 0
#
# while end < n:
#     while end < n and laser[end] != ')':  # ) 를 만나면 종료
#         end += 1
#     if end >= n:
#         break
#
#     start = end
#     while start >= 0 and laser[start] != '(':  # ( 를 만나면 종료
#         start -= 1
#     if start < 0:
#         break
#
#     ct += sum(1 for x in laser[start:end] if x == "1") + 1
#
#     laser[end] = "0"
#     laser[start] = "0"
#
#     end += 1
#
# print(ct)

# stack = []
# ct = 0
#
# for i in range(len(laser)):
#     if laser[i] == '(':
#         stack.append('(')
#     else:
#         stack.pop()
#
#         if laser[i-1] == '(':
#             ct += len(stack)
#         else:
#             ct += 1
#
# print(ct)