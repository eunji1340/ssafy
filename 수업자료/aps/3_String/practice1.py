s = 'string'
s = s[::-1]
print(s, type(s))

s = 'abcd'
s = list(s)
s.reverse()
s = ''.join(s)
print(s)