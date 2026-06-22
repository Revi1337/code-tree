def solution(cm, cd, tm, td):
    mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 1

    while True:
        if cm == tm and cd == td:
            break

        ans += 1
        cd += 1

        if cd > mdays[cm]:
            cm += 1
            cd = 1

    return ans

m1, d1, m2, d2 = map(int, input().split())
print(solution(m1, d1, m2, d2))
