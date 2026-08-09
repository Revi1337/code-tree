drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
dat = {
    '/': {0:1, 1:0, 2:3, 3:2},
    '\\': {0:3, 1:2, 2:1, 3:0}
}

def solution(N, grid, K):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    d = 1
    edges = [(0, 0)]
    row = col = 0
    while len(edges) < 4 * N:
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol):
            d = (d + 1) % 4
            edges.append((row, col))
        else:
            edges.append((nrow, ncol))
            row, col = nrow, ncol

    dd = [2, 3, 0, 1] # base on drow & dcol
    row, col = edges[K - 1]
    d = dd[(K - 1) // N]
    d = dat[grid[row][col]][d]

    ans = 1
    while inside(row, col):
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol):
            return ans
        row, col = nrow, ncol
        sign = grid[row][col]
        d = dat[sign][d]
        ans += 1

    return ans

N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]
K = int(input())
print(solution(N, grid, K))
