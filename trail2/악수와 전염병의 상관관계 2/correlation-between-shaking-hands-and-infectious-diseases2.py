def solution(n, k, p, t, arr):
    cnts, ans = [k] * (n + 1), [0] * (n + 1)
    arr.sort(key=lambda x: x[0])
    ans[p] = 1
    for _, x, y in arr:
        if cnts[x] and cnts[y]:
            cnts[x], cnts[y] = cnts[x] - 1, cnts[y] - 1
            ans[x] = ans[y] = 1

    return ''.join(map(str, ans[1:]))

n, k, p, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(t)]
print(solution(n, k, p, t, arr))