def solution(n, k, p, t, arr):
    cnts, ans = [[0] * (n + 1) for _ in range(2)]
    arr.sort(key=lambda x: x[0])
    cnts[p], ans[p] = k, 1

    for _, x, y in arr:
        if ans[x] and cnts[x] > 0:
            cnts[x] -= 1
            if not ans[y]:
                cnts[y], ans[y] = k, 1
        if ans[y] and cnts[y] > 0:
            cnts[y] -= 1
            if not ans[x]:
                cnts[x], ans[x] = k, 1

    return ''.join(map(str, ans[1:]))

n, k, p, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(t)]
print(solution(n, k, p, t, arr))
