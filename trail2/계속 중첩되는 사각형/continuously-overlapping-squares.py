def solution(N, arrs):
    OFFSET = 100
    grid = [[0] * 201 for _ in range(201)]

    for i, (x1, y1, x2, y2) in enumerate(arrs):
        color = 1 if i % 2 == 0 else 2
        start_x, end_x = min(x1, x2), max(x1, x2)
        start_y, end_y = min(y1, y2), max(y1, y2)
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                grid[x + OFFSET][y + OFFSET] = color

    blue_area = 0
    for x in range(201):
        for y in range(201):
            if grid[x][y] == 2:
                blue_area += 1

    return blue_area

N = int(input())
arrs = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(N, arrs))
