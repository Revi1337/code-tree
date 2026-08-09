drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    arr = [[0] * N for _ in range(N)]
    row = col = N - 1
    d = 3
    st = N ** 2
    arr[row][col] = st
    counter = N ** 2 - 1

    while counter > 0:
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol]:
            d = (d + 1) % 4
            continue

        st -= 1
        arr[nrow][ncol] = st
        row, col = nrow, ncol
        counter -= 1

    for line in arr:
        print(*line)

N = int(input())
solution(N)