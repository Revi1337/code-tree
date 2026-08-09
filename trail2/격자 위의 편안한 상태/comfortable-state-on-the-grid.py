drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, points):

    inside = lambda row, col: 1 <= row <= N and 1 <= col <= N

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for row, col in points:
        arr[row][col] = 1
        cnt = 0
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol) and arr[nrow][ncol]:
                cnt += 1
        if cnt == 3:
            print(1)
        else:
            print(0)

N, M = map(int, input().rstrip().split())
points = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
solution(N, M, points)
