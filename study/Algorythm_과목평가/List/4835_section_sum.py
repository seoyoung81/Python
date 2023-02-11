T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 정수의 개수, 구간의 개수
    numbers = list(map(int, input().split()))   # N개의 정수

    total_list = [0] * (N-M+1)  # range 작성 잘하자

    for i in range(0, N-M+1):
        for j in range(i, i+M): # M개의 합 구하기 j를 이동시키면서 구하고 싶을 땐 j의 범위에 i를 반영시켜주자
            total_list[i] += numbers[j]
    # print(total_list)

    # print(f'#{tc} {max(total_list) - min(total_list)}')
    maxV = minV = total_list[0]
    m = len(total_list)
    # 최댓값 구하기
    for i in range(1, m):
        if maxV < total_list[i]:
            maxV = total_list[i]
    # 최솟값 구하기
    for i in range(1, m):
        if minV > total_list[i]:
            minV = total_list[i]

    result = maxV - minV
    print(f'#{tc} {result}')