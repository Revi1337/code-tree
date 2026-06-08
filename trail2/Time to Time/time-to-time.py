import sys

sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

def solution(a, b, c, d):
    fro, to = (60 * a) + b, (60 * c) + d
    return to - fro

a, b, c, d = map(int, input().split())
print(solution(a, b, c, d))