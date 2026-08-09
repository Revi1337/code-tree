drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, T, str, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    row = col = N // 2
    d, ans = 0, arr[row][col]
    for c in str:
        if c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
        else:
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol):
                ans += arr[nrow][ncol]
                row, col = nrow, ncol

    return ans

N, T = map(int, input().rstrip().split())
str = input().rstrip()
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(N, T, str, board))
