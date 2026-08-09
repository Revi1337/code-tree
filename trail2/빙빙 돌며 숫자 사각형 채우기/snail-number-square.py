drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    ans = [[0] * M for _ in range(N)]
    row = col = 0
    st = 1
    ans[row][col] = st
    st += 1
    d, cnt = 1, N * M - 1

    while cnt > 0:
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or ans[nrow][ncol]:
            d = (d + 1) % 4
            continue

        ans[nrow][ncol] = st
        row, col = nrow, ncol
        st += 1
        cnt -= 1

    for line in ans:
        print(*line)

n, m = map(int, input().rstrip().split())
solution(n, m)
