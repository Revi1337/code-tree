import sys

input = sys.stdin.readline
sys.setrecursionlimit(300000)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_v, to_v, weight = zip(*edges)
from_v = list(from_v)
to_v = list(to_v)
weight = list(weight)

graph = [[] for i in range(n)]

for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

parent = [-1] * n
par_w = [0] * n

height = [0] * n
sub_diam = [0] * n


def dfs1(cur, prev):
    parent[cur] = prev

    best1 = 0
    best2 = 0

    for nxt, w in graph[cur]:
        if nxt == prev:
            continue

        par_w[nxt] = w
        dfs1(nxt, cur)

        h = height[nxt] + w

        if h > best1:
            best2 = best1
            best1 = h
        elif h > best2:
            best2 = h

        sub_diam[cur] = max(sub_diam[cur], sub_diam[nxt])

    height[cur] = best1
    sub_diam[cur] = max(sub_diam[cur], best1 + best2)


dfs1(0, -1)

out_height = [0] * n
out_diam = [0] * n


def dfs2(cur, prev):
    child_h = []
    child_d = []

    for nxt, w in graph[cur]:
        if nxt == prev:
            continue

        child_h.append((height[nxt] + w, nxt))
        child_d.append((sub_diam[nxt], nxt))

    child_h.sort(reverse=True)
    child_d.sort(reverse=True)

    for nxt, w in graph[cur]:
        if nxt == prev:
            continue

        best_h = out_height[cur]

        for h, node in child_h:
            if node != nxt:
                best_h = max(best_h, h)
                break

        out_height[nxt] = best_h + w

        diam_val = out_diam[cur]

        for d, node in child_d:
            if node != nxt:
                diam_val = max(diam_val, d)
                break

        branches = [out_height[cur]]

        for h, node in child_h:
            if node != nxt:
                branches.append(h)

        branches.sort(reverse=True)

        while len(branches) < 2:
            branches.append(0)

        diam_val = max(diam_val, branches[0] + branches[1])

        out_diam[nxt] = diam_val

        dfs2(nxt, cur)


dfs2(0, -1)

answer = 0

for node in range(1, n):
    answer = max(
        answer,
        sub_diam[node] + out_diam[node] + par_w[node]
    )

print(answer)