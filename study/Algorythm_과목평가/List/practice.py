board = [[0] * 10 for _ in range(10)]

T = int(input())
for i in range(1, T + 1):
    total = int(input())
    for _ in range(total):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                board[i][j] += color

    count = 0

    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                count += 1
    print(count)