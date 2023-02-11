# 연습문제1
T = int(input())    # 테스트 케이스의 개수
for test_case in range(1, T+1):
    N = int(input())    # N X N arr
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2d arr

    total = 0
    for i in range(N):
        for j in range(N):
            for dx, dy in [-1, 0], [0, 1], [1, 0], [0, -1]: # 상우하좌
                ni = i + dx
                nj = j + dy
                if 0 <= ni < N and 0 <= nj < N: # 밖으로 튀어나가지 않은 상황에서
                    sub = abs(arr[i][j] - arr[ni][nj])  # 주변 값과의 차의 절댓값 구하기
                    total += sub    # 총합 구하기

    print(f'#{test_case} {total}')


