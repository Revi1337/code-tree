def solution(N, arr):
    ans = [[0] * 201 for _ in range(201)]
    for x1, y1, x2, y2 in arr:
        for row in range(min(x1, x2), max(x1, x2)):
            for col in range(min(y1, y2), max(y1, y2)):
                ans[row + 100][col + 100] = 1

    return sum(sum(line) for line in ans)

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(N, arr))