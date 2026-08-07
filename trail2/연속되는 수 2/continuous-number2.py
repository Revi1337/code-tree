def solution(N, arr):
    ans = 0
    length = 1
    for idx in range(N):
        if idx == 0 or arr[idx - 1] != arr[idx]:
            ans = max(ans, length)
            length = 1  
        else:
            length += 1
    return ans
        
N = int(input())
arr = [int(input()) for _ in range(N)]
print(solution(N, arr))