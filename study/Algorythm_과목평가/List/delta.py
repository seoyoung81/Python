arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

for i in range(4):
    for j in range(4):
        for dx, dy in [-1, 0], [0, 1], [1, 0], [0, -1]:     # 하좌상우
            ni = i + dx
            nj = j + dy
            if 0 <= ni < 4 and 0 <= nj < 4:
                print(arr[ni][nj])

