T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # N X N array
    arr = [[0] * N for _ in range(N)]   # 0 으로 채운 N X N 2d arr

    i = j = 0
    k = 0
    cnt = 2
    arr[0][0] = 1
    dx = [0, 1, 0, -1]  # 우하좌상
    dy = [1, 0, -1, 0]

    while cnt <= N * N:     # 숫자가 N 제곱이 될 때까지
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
