def solution(A, B, N):
    N, cost = str(N), 0
    for idx in range(len(N)):
        if int(N[idx]):
            cost += int(N[idx]) * A ** idx

    ans = []
    while cost > 0:
        ans.append(cost % B)
        cost //= B

    return ''.join(map(str, ans[::-1])) if ans else 0

A, B = map(int, input().split())
N = int(input())
print(solution(A, B, N))