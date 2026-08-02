def solution(binary):
    ans, sbin = 0, str(binary)
    for idx in range(len(sbin)):
        if sbin[idx] == '1':
            cost = 2 ** (len(sbin) - 1 - idx)
            ans += cost
    return ans

binary = int(input())
print(solution(binary))