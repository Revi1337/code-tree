def solution(N, M, A, B):
    T = sum(t for _, t in A)
    psum1, psum2 = [[0] * (T + 1) for _ in range(2)]

    ct = 0
    for v, t in A:
        while t > 0:
            t -= 1
            ct += 1
            psum1[ct] = psum1[ct - 1] + v
    ct = 0
    for v, t in B:
        while t > 0:
            t -= 1
            ct += 1
            psum2[ct] = psum2[ct - 1] + v

    ans = 1
    for t in range(2, len(psum1)):
        diff1 = psum1[t] - psum2[t]
        diff2 = psum1[t - 1] - psum2[t - 1]
        if not diff1 and not diff2:
            continue
        if not (diff1 > 0 and diff2 > 0 or diff1 < 0 and diff2 < 0):
            ans += 1

    return ans

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, A, B))