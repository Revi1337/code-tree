drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    arr = [[0] * M for _ in range(N)]
    row, col, st = 0, 0, 1
    arr[row][col] = st
    d = 2
    counter = N * M - 1

    while counter > 0:
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol]:
            d = (d - 1) % 4
            continue

        st += 1
        arr[nrow][ncol] = st
        row, col = nrow, ncol
        counter -= 1

    for line in arr:
        print(*line)

N, M = map(int, input().rstrip().split())
solution(N, M)