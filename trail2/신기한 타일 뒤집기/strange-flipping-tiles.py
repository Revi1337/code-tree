def solution(n, segments):
    WHITE, BLACK = 1, -1,
    arr = [0] * (((1000 * 100) * 2) + 1)
    curr = (1000 * 100 * 2) // 2
    for dist, d in segments:
        dist = int(dist)
        if d == 'R':
            for v in range(curr, curr + dist):
                arr[v] = BLACK
            curr = curr + dist - 1
        else:
            for v in range(curr - dist + 1, curr + 1):
                arr[v] = WHITE
            curr = curr - dist + 1

    ans = [0] * 2
    for color in arr:
        if color == WHITE:
            ans[0] += 1
        elif color == BLACK:
            ans[1] += 1

    return ans

n = int(input())
segments = [list(input().split()) for _ in range(n)]
print(*solution(n, segments))

