def solution(n, segments):
    arr = [0] * ((100 * 10 * 2) + 1)
    curr = (100 * 10 * 2) // 2
    for dist, dir in segments:
        dist = int(dist)
        if dir == 'L':
            for v in range(curr, curr - dist, -1):
                arr[v] += 1
            curr -= dist
        else:
            for v in range(curr, curr + dist):
                arr[v] += 1
            curr += dist

    return len([cnt for cnt in arr if cnt >= 2])

n = int(input())
segments = [list(input().split()) for _ in range(n)]
print(solution(n, segments))
