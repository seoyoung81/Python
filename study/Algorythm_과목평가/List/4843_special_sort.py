T = int(input())    # test_case
for test_case in range(1, T+1):
    N = int(input())    # num count
    numbers = map(str, input().split())

    # numbers sort
    numbers = sorted(numbers, reverse=True)

    # special sort
    numbers_list = [] * N
    for i in range(N):
        for j in range(N-1, N//2, -1):
            if i % 2:   # odd
                numbers_list[i] = numbers[j]
        for j in range(N//2):
            if not i % 2:
                numbers_list[i] = numbers[j]
    print(numbers_list)