drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]
dat = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

def solution(n, moves):
    curr = [0, 0]
    for d, cnt in moves:
        cnt = int(cnt)
        curr[0], curr[1] = curr[0] + (dcol[dat[d]] * cnt), curr[1] + (drow[dat[d]] * cnt)
    print(*curr)

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
solution(n, moves)