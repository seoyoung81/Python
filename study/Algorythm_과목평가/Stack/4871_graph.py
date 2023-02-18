def dfs(v):
    visited[v] = 1  # 방문했다면 1 찍기
    stack.append(v)

    for w in range(1, V+1):
        if arr[v][w] == 1 and visited[w] == 0:  # 간선이 연결되어 있고 방문한 적이 없다면
            dfs(w)



T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())    # 노드, 간선 개수
    arr = [[0] * (V+1) for _ in range(V+1)]     # data를 담을 리스
    result = 0
    for _ in range(E):
        node, road = map(int, input().split())      # 간선과 노드 연결 정보트
        arr[node][road] = 1
    start, end = map(int, input().split())    # 시작, 끝
    stack = []
    visited = [0] * (V+1)

    dfs(start)


    if end in stack:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')

