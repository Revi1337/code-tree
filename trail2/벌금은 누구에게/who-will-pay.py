def solution(n, m, k, arr):
    ans = [0] * (n + 1)
    for s in arr:
        ans[s] += 1
        for idx in range(n + 1):
            if ans[idx] == k:
                return idx

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(m)]
print(solution(n, m, k, arr))
