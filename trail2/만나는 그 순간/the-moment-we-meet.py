def solution(N, M, A, B):
    arr1, arr2 = [[0] * 1_000_001 for _ in range(2)]
    cc = ct = 0
    for d, t in A:
        t = int(t)
        if d == 'R':
            while t > 0:
                t -= 1
                ct += 1
                cc += 1
                arr1[ct] = cc
        else:
            while t > 0:
                t -= 1
                ct += 1
                cc -= 1
                arr1[ct] = cc

    cc = ct = 0
    for d, t in B:
        t = int(t)
        if d == 'R':
            while t > 0:
                t -= 1
                ct += 1
                cc += 1
                arr2[ct] = cc
        else:
            while t > 0:
                t -= 1
                ct += 1
                cc -= 1
                arr2[ct] = cc

    for idx in range(len(arr1)):
        if arr1[idx] and arr2[idx] and arr1[idx] == arr2[idx]:
            return idx

    return -1

N, M = map(int, input().split())
A = [input().split() for _ in range(N)]
B = [input().split() for _ in range(M)]
print(solution(N, M, A, B))