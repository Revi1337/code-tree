drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(commands):
    row = col = 0
    d = 0
    for t, c in enumerate(commands, start=1):
        if c == 'L':
            d = (d - 1) % 4
        elif c == 'R':
            d = (d + 1) % 4
        else:
            nrow, ncol = row + drow[d], col + dcol[d]
            row, col = nrow, ncol
            if row == 0 and col == 0:
                return t
    return -1

commands = input().rstrip()
print(solution(commands))
