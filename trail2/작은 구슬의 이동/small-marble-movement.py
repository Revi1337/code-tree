drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
dat = {'U': 0, 'L': 1, 'D': 2, 'R': 3}

def solution(N, T, R, C, D):

    inside = lambda row, col: 1 <= row <= N and 1 <= col <= N

    row, col = map(int, [R, C])
    d = dat[D]
    while T > 0:
        T -= 1
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol):
            d = (d + 2) % 4
        else:
            row, col = nrow, ncol

    print(row, col)

N, T = map(int, input().rstrip().split())
R, C, D = input().rstrip().split()
solution(N, T, R, C, D)

