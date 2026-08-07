def solution(arr):
    ans = [[0] * 265 for _ in range(265)]
    for row, col in arr:
        for nrow in range(row, row + 8):
            for ncol in range(col, col + 8):
                ans[nrow + 100][ncol + 100] = 1

    return sum(sum(line) for line in ans)

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(arr))
