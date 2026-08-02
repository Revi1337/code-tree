def solution(n, k, commands):
    arr = [0] * (n + 1)
    for n1, n2 in commands:
        for n in range(n1, n2 + 1):
            arr[n] += 1

    return max(arr)


n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
print(solution(n, k, commands))
