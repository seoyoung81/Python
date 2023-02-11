# 낙차 구하기 -> 내 뒤에 나보다 작은 애가 몇 개?
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 막대 개수
    numbers = list(map(int, input().split()))   # 막대의 크기 리스트로 받기

    cnt = [0] * N
    for i in range(N-1):
        for j in range(i+1, N):
            if numbers[i] > numbers[j]: # 내 뒤에 있는 것보다 내가 크다면
                cnt[i] += 1                # 개수 추가

    # 최댓값 구하기
    maxV = cnt[0]
    for i in range(1, N):
        if maxV < cnt[i]:
            maxV = cnt[i]

    print(f'#{tc} {maxV}')