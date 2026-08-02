dom = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dom2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(m1, d1, m2, d2):

    def tot_days(m, d):
        return sum(dom2[:m]) + d

    diff = tot_days(m2, d2) - tot_days(m1, d1)
    return dom[diff % 7]

m1, d1, m2, d2 = map(int, input().split())
print(solution(m1, d1, m2, d2))
