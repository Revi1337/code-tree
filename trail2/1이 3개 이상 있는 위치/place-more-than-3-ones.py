drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, arr):

    inside = lambda row, col: 0 <= row < n and 0 <= col < n

    ans = 0
    for row in range(n):
        for col in range(n):
            cnt = 0
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol) and arr[nrow][ncol]:
                    cnt += 1
            if cnt >= 3:
                ans += 1

    return ans

n = int(input())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
print(solution(n, grid))

