drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

def solution(dirs):
    curr = [0, 0]
    cd = 0
    for d in dirs:
        if d == 'R':
            cd = (cd + 1) % 4
        elif d == 'L':
            cd = (cd - 1) % 4
        else:
            curr[0], curr[1] = curr[0] + dcol[cd], curr[1] + drow[cd]
    print(*curr)

dirs = input().rstrip()
solution(dirs)
