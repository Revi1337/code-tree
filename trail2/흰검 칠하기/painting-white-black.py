def solution(n, segments):
    EMPTY, WHITE, BLACK, GRAY = 0, 1, -1, 1e9
    arr = [0] * (((1000 * 100) * 2) + 1)
    cnts = {idx: [0, 0] for idx in range(len(arr))}
    curr = (1000 * 100 * 2) // 2
    for dist, d in segments:
        dist = int(dist)
        if d == 'L':
            for v in range(curr - dist + 1, curr + 1):
                if arr[v] == GRAY:
                    continue
                cnts[v][0] += 1
                if cnts[v][0] >= 2 and cnts[v][1] >= 2:
                    arr[v] = GRAY
                else:
                    arr[v] = WHITE
            curr = curr - dist + 1
        else:
            for v in range(curr, curr + dist):
                if arr[v] == GRAY:
                    continue
                cnts[v][1] += 1
                if cnts[v][0] >= 2 and cnts[v][1] >= 2:
                    arr[v] = GRAY
                else:
                    arr[v] = BLACK
            curr = curr + dist - 1

    ans = [0] * 3
    for color in arr:
        if color == WHITE:
            ans[0] += 1
        elif color == BLACK:
            ans[1] += 1
        elif color == GRAY:
            ans[2] += 1

    return ans

n = int(input())
segments = [list(input().split()) for _ in range(n)]
print(*solution(n, segments))
