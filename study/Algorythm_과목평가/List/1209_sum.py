T = 10   # test_case 10
for test_case in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row_arr = col_arr = dia_arr = [[0] * 100 for _ in range(100)]
    # row_sum & col_sum
    for i in range(100):
        for j in range(100):
            row_arr[i].append(arr[i][j])
            row_arr[i].append(arr[j][i])

    # print(row_arr)
    # print(col_arr)

    # i = j
    for i in range(100):
        row_arr[i].append(arr[i][i])
        # i != j
        row_arr[i].append(arr[i][99-i])

    total = 0
    for i in range(100):
        for j in range(100):
            total += row_arr[i][j]


    print(f'{test_case} {max(total)}')

