N = 4  # Example, set this to the desired number
used = [False] * (N + 1)  # Used array to track visited numbers
paths = []  # To store all valid paths

def find_path(cnt, path):
    if cnt == N:
        path.append(1)  # Assuming you want to append 1 at the end of the path
        paths.append(path[:])  # Store a copy of the path
        path.pop()
        return

    for num in range(2, N + 1):
        if not used[num]:
            used[num] = True
            path.append(num)
            find_path(cnt + 1, path)  # Recursive call
            path.pop()
            used[num] = False

# Start the pathfinding from an empty path
find_path(1, [1])

print(paths)  # Print all paths
