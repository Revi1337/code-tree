def solution(n, m, A, B):
    atsm, btsm = sum(int(t) for t, _ in A), sum(int(t) for t, _ in B)
    mnt, mxt = min(atsm, btsm), max(atsm, btsm)
    arr1, arr2 = [[[0, 0] for _ in range(mxt + 1)] for _ in range(2)]

    ct = cd = 0
    for t, d in A:
        t = int(t)
        if d == 'R':
            while t > 0:
                t -= 1
                ct += 1
                cd += 1
                arr1[ct][0] = cd
                arr1[ct][1] = arr1[ct - 1][0]
        else:
            while t > 0:
                t -= 1
                ct += 1
                cd -= 1
                arr1[ct][0] = cd
                arr1[ct][1] = arr1[ct - 1][0]

    ct = cd = 0
    for t, d in B:
        t = int(t)
        if d == 'R':
            while t > 0:
                t -= 1
                ct += 1
                cd += 1
                arr2[ct][0] = cd
                arr2[ct][1] = arr2[ct - 1][0]
        else:
            while t > 0:
                t -= 1
                ct += 1
                cd -= 1
                arr2[ct][0] = cd
                arr2[ct][1] = arr2[ct - 1][0]

    if arr1[mxt] == [0, 0]:
        for t in range(mnt, mxt + 1):
            arr1[t] = arr1[mnt]
    elif arr2[mxt] == [0, 0]:
        for t in range(mnt, mxt + 1):
            arr2[t] = arr2[mnt]

    ans = 0
    for t in range(1, mxt + 1):
        if arr1[t][0] == arr2[t][0] and arr1[t][1] != arr2[t][1]:
            ans += 1

    return ans

n, m = map(int, input().split())
A = [input().split() for _ in range(n)]
B = [input().split() for _ in range(m)]
print(solution(n, m, A, B))