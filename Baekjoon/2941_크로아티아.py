string = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

def find_alpha(string, alpha):
    i = 0
    ct = 0

    while i < len(string):
        matched = False
        for a in alpha:
            if string[i:i+len(a)] == a:
                ct += 1
                i += len(a)
                matched = True
                break
        if not matched:
            ct += 1
            i += 1

    return ct

print(find_alpha(string, alpha))