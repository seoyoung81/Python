def dfs(v, w):
    visited[v][w] = 1   # 방문하면 1 찍기

    for i, j in [[v, w-1], [v+1, w], [v, w+1], [v-1, w]]:
        if 0 <= i < N and 0 <= j < N:
            if maze[i][j] == 3:
                global s
                s = 1
            elif maze[i][j] == 0 and visited[i][j] == 0:
                dfs(i, j)
    return s

T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # N X N array
    maze = [list(map(int, input())) for _ in range(N)]  # 2d array
    visited = [[0] * N for _ in range(N)]
    s = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                a = i
                b = j
    print(dfs(a, b))
