def solution(N, T, arr):
    ans = curr = 0
    for x in arr:
        if x > T:
            curr += 1
            ans = max(ans, curr)
        else:
            curr = 0
    return ans

N, T = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(N, T, arr))