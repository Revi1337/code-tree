dom = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dom2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(m1, d1, m2, d2, A):

    def get_days(m, d):
        return sum(dom2[:m]) + d

    diff = get_days(m2, d2) - get_days(m1, m2)

    return diff // 7 + 1 if diff % 7 > dom.index(A) else diff // 7

m1, d1, m2, d2 = map(int, input().split())
A = input().rstrip()
print(solution(m1, d1, m2, d2, A))
