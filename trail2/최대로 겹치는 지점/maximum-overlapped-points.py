def solution(n, commands):
    off = min(commands, key=lambda x: x[0])[0]
    if off > 0:
        commands = [[x1 + off, x2 + off] for x1, x2 in commands]

    arr = [0] * 201
    for v1, v2 in commands:
        if v1 <= v2:
            for v in range(v1, v2 + 1):
                arr[v] += 1

    return max(arr)

n = int(input())
commands = [tuple(map(int, input().split())) for _ in range(n)]
print(solution(n, commands))