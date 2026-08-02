def solution(N):
    N, cost = str(N)[::-1], 0
    for idx in range(len(N)):
        if N[idx] == '1':
            cost += 2 ** idx

    cost *= 17

    ans = []
    while cost > 0:
        ans.append(cost % 2)
        cost //= 2

    return ''.join(map(str, ans[::-1])) if ans else 0

N = int(input())
print(solution(N))