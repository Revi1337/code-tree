def solution(N, B):
    ans = []
    while N > 0:
        ans.append(N % B)
        N //= B

    return ''.join(map(str, ans[::-1])) if ans else 0

N, B = map(int, input().split())
print(solution(N, B))