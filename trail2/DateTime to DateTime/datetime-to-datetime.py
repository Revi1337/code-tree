D, H, M = 11, 11, 11

def solution(a, b, c):
    ans = ((a - D) * 24 * 60) + ((b - H) * 60) + (c - M)
    return ans if ans > 0 else -1

a, b, c = map(int, input().split())
print(solution(a, b, c))


