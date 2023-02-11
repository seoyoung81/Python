T = 10  # 10 test case
for test_case in range(1, T+1):
    dump = int(input()) # dump number
    numbers = list(map(int, input().split()))   # box
    # 정렬 한 후에 가장 큰 값에서 가장 작은 값을 빼주고 다시 재정렬하자
    m = len(numbers)    # box 개수
    result = 0
    for i in range(dump):
        # numbers.sort()
        # 선택 정렬하기
        for j in range(m-1):
            min_idx = j
            for k in range(j+1, m):
                if numbers[min_idx] > numbers[k]:
                    min_idx = k
            numbers[j], numbers[min_idx] = numbers[min_idx], numbers[j]

        numbers[-1] -= 1
        numbers[0] += 1
        if numbers[-1] - numbers[0] < 2:
            result = 1
        else:
            result = numbers[-2] - numbers[1]
    print(f'#{test_case} {result}')

