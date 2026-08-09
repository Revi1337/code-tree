drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    arr = [[0] * M for _ in range(N)]
    row, col, st, d = 0, 0, 0, 0
    arr[row][col] = chr(st + 65)
    counter = N * M - 1

    while counter > 0:
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol]:
            d = (d + 1) % 4
            continue

        st = (st + 1) % 26
        arr[nrow][ncol] = chr(st + 65)
        row, col = nrow, ncol
        counter -= 1

    for line in arr:
        print(*line)

N, M = map(int, input().rstrip().split())
solution(N, M)