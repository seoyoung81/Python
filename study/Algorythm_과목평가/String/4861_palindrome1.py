T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # n*n arr, word
    row_arr = [list(map(str, input())) for _ in range(N)]
    # col_arr
    col_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            col_arr[i][j] = row_arr[j][i]

    # 회문 찾기 (가로)
    for i in range(N):
        for j in range(N-M+1):
            if row_arr[i][j:j+M] == row_arr[i][j:j+M][::-1]:
                print(''.join(row_arr[i][j:j+M]))

    # # 회문 찾기 (세로)
    for i in range(N):
        for j in range(N-M+1):
            if col_arr[i][j:j+M] == col_arr[i][j:j+M][::-1]:
                print(''.join(col_arr[i][j:j+M]))