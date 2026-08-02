def solution(binary):
    ans, sbin = 0, str(binary)[::-1]
    for idx in range(len(sbin)):
        if sbin[idx] == '1':
            cost = 2 ** idx
            ans += cost
    return ans

binary = int(input())
print(solution(binary))


# import sys
#
# sys.stdin = open('input.txt', 'r', encoding='utf-8')
# input = sys.stdin.readline
#
# """
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-convert-to-decimal/description
# """
#
# def solution(binary):
#     ans, sbin = 0, str(binary)
#     for idx in range(len(sbin)):
#         if sbin[idx] == '1':
#             cost = 2 ** (len(sbin) - 1 - idx)
#             ans += cost
#     return ans
#
# binary = int(input())
# print(solution(binary))
