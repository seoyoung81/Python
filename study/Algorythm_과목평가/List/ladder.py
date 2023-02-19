import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, 11):
    tc = int(input())   # test cass number input
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 100 X 100 array

    # 도착 지점 구하기
    # for i in range(100):
    #     if ladder[-1][i] == 2:  # 2 인 곳에서 출발하자
    #         start = ladder[-1][i]

    # 도착 지점 구하기 2
    start = ladder[-1].index(2) # 2인 곳의 인덱스 값

    dx = [1, -1]
    dy = [0, 0]

    # 위로 99칸 올라갈 예정
    move = 99   # 0 이되면 도착 한 것

    while move != 0:
        for i in range(2):  # 좌 우 검사
            end = True
            # 움직일 수 있다면
            if (0 <= start + dx[i] <= 99) and ladder[move + dy[i]][start + dx[i]] == 1:
                while end:  # 종료 조건이 거짓일 때까지
                    if (0 <= start + dx[i] <= 99) and ladder[move + dy[i]][start + dx[i]] == 1:
                        start += dx[i]  # 움직인다
                    else:
                        end = False     # 더 이상 움직 일 수 없다면 끝낸다
                break
        move -= 1

    print(f'#{test_case}', start)
