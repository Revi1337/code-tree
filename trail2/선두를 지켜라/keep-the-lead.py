def solution(n, m, A, B):
    arr1, arr2 = [[0] * 1_000_001 for _ in range(2)]

    ct = cv = 0
    for v, t in A:
        while t > 0:
            t -= 1
            cv += v
            ct += 1
            arr1[ct] = cv
    ct = cv = 0
    for v, t in B:
        while t > 0:
            t -= 1
            cv += v
            ct += 1
            arr2[ct] = cv

    diffs = []
    for t in range(1, len(arr1)):
        if arr1[t] - arr2[t]:
            diffs.append(arr1[t] - arr2[t])

    ans = 0
    for t in range(1, len(diffs)):
        if (diffs[t] > 0 and diffs[t - 1] < 0) or (diffs[t] < 0 and diffs[t - 1] > 0):
            ans += 1
    return ans

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, A, B))
