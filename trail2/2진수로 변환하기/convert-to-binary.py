def solution(n):
    ans = []
    while n != 0:
        ans.append(n % 2)
        n //= 2

    return ''.join(map(str, ans[::-1]))

n = int(input())
print(solution(n))
