def solution(N, arr):
    ans = curr = 1
    for idx in range(1, N):
        if arr[idx] > arr[idx - 1]:
            curr += 1
        else:
            ans = max(ans, curr)
            curr = 1
    return max(ans, curr)

N = int(input())
arr = [int(input()) for _ in range(N)]
print(solution(N, arr))