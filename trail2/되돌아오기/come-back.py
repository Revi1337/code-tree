drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
dat = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

def solution(N, moves):
    row = col = 0
    ct = 0
    for d, t in moves:
        d, t = dat[d], int(t)
        while t > 0:
            t -= 1
            ct += 1
            nrow, ncol = row + drow[d], col + dcol[d]
            row, col = nrow, ncol
            if row == 0 and col == 0:
                return ct
    return -1

N = int(input())
moves = [tuple(input().rstrip().split()) for _ in range(N)]
print(solution(N, moves))