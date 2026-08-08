def solution(n, m, A, B):
    arr1, arr2 = [0], [0]

    for t, d in A:
        t = int(t)
        move = 1 if d == 'R' else -1
        for _ in range(t):
            arr1.append(arr1[-1] + move)

    for t, d in B:
        t = int(t)
        move = 1 if d == 'R' else -1
        for _ in range(t):
            arr2.append(arr2[-1] + move)

    ta = len(arr1) - 1
    tb = len(arr2) - 1
    mxt = max(ta, tb)

    while len(arr1) < mxt + 1:
        arr1.append(arr1[-1])
    while len(arr2) < mxt + 1:
        arr2.append(arr2[-1])

    ans = 0
    for t in range(1, mxt + 1):
        if arr1[t] == arr2[t] and arr1[t - 1] != arr2[t - 1]:
            ans += 1

    return ans

n, m = map(int, input().split())
A = [input().split() for _ in range(n)]
B = [input().split() for _ in range(m)]
print(solution(n, m, A, B))