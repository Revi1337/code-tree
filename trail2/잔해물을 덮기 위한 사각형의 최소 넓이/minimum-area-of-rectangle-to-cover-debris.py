def solution(arrs):
    OFFSET = 1000
    grid = [[0] * 2001 for _ in range(2001)]

    for idx, (x1, y1, x2, y2) in enumerate(arrs, start=1):
        start_x, end_x = min(x1, x2), max(x1, x2)
        start_y, end_y = min(y1, y2), max(y1, y2)
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                grid[x + OFFSET][y + OFFSET] = idx

    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    found = False

    for x in range(2001):
        for y in range(2001):
            if grid[x][y] == 1:
                found = True
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    if not found:
        return 0
    return (max_x - min_x + 1) * (max_y - min_y + 1)

N = 2
arrs = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(arrs))