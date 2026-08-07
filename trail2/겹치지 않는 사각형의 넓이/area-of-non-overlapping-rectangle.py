def solution(arrs):
    arr1, arr2, arr3 = arrs
    ans = [[0] * 2001 for _ in range(2001)]
    for row in range(min(arr1[0], arr1[2]), max(arr1[0], arr1[2])):
        for col in range(min(arr1[1], arr1[3]), max(arr1[1], arr1[3])):
            ans[row + 1000][col + 1000] = 1
    for row in range(min(arr2[0], arr2[2]), max(arr2[0], arr2[2])):
        for col in range(min(arr2[1], arr2[3]), max(arr2[1], arr2[3])):
            ans[row + 1000][col + 1000] = 1
    for row in range(min(arr3[0], arr3[2]), max(arr3[0], arr3[2])):
        for col in range(min(arr3[1], arr3[3]), max(arr3[1], arr3[3])):
            ans[row + 1000][col + 1000] = 0

    return sum(sum(line) for line in ans)

N = 3
arrs = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(arrs))
