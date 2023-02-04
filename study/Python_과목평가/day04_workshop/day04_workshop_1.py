N = int(input())    # 정수 N을 입력

for i in range(1, N+1):
    if N % i == 0:
        print(i, end = ' ')