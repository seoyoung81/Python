T = int(input())    # test_case
for test_case in range(1, T+1):
    N = int(input())    # N X N arr
    arr = [[0] * N for _ in range(N)]
    # delta
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 2
    arr[0][0] = 1

    i = j = k = 0
    while cnt < N ** 2 + 1:
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i = ni
            j = nj
        else:
            k += 1
            if k > 3:
                k = k % 4
    print(arr)
























    # delta
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 2
    arr[0][0] = 1

    i = j = 0
    k = 0
    while cnt < N**2 + 1:
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i = ni
            j = nj
        else:
            k += 1
            if k > 3:
                k = k % 4
    print(arr)

