T = int(input())    # 테스트 케이스의 개수

for tc in range(1, T + 1):
    N = int(input())    # N * N
    arr = [[0] * N for _ in range(N)]    # N * N 행렬
    # print(arr)
    # 그냥 순서대로 넣기
    # cnt = 1
    # for i in range(N):
    #     for j in range(N):
    #         if j == N - 1
    #         arr[i][j] += cnt
    #         cnt += 1
    # print(arr)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 2
    arr[0][0] = 1

    i = j = 0
    k = 0
    while cnt < N * N + 1:
        ni, nj = i + dx[k], j + dy[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i = ni
            j = nj
        else:   # 범위에서 벗어나면
            k += 1
            if k > 3:
                k = k % 4
    print(f'#{tc}')
    # print(arr)
    for i in range(N):

        print(' '.join(str(n) for n in arr[i]))
