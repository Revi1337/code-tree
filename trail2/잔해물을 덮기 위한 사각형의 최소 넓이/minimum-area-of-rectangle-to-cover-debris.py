def solution(arrs):
    ans = [[0] * 2001 for _ in range(2001)]
    for idx, (x1, y1, x2, y2) in enumerate(arrs, start=1):
        for nrow in range(min(x1, x2), max(x1, x2)):
            for ncol in range(min(y1, y2), max(y1, y2)):
                ans[nrow + 1000][ncol + 1000] = idx

    cnt = 0
    for nrow in range(min(arrs[0][0], arrs[0][2]), max(arrs[0][0], arrs[0][2])):
        for ncol in range(min(arrs[0][1], arrs[0][3]), max(arrs[0][1], arrs[0][3])):
            cnt += 1

    return cnt

N = 2
arrs = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(arrs))