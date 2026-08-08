def solution(N, T, arr):
    ans = curr = 1 if arr[0] > T else 0
    for idx in range(1, N):
        if arr[idx] > T and arr[idx - 1] > T:
            curr += 1
        else:
            ans = max(ans, curr)
            curr = 0
    return max(ans, curr)

N, T = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(N, T, arr))