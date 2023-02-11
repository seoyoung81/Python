T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 양수의 개수
    numbers = list(map(int, input().split()))
    m = len(numbers)
    # 최솟값 구하기
    minV = maxV = numbers[0]
    for i in range(1, m):
        if minV > numbers[i]:
            minV = numbers[i]
    # 최댓값 구하기
    for i in range(1, m):
        if maxV < numbers[i]:
            maxV = numbers[i]

    result = maxV - minV
    print(f'#{tc} {result}')
