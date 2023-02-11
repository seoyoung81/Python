T = int(input())    # testcase
for test_case in range(1, T+1):
    N, k = map(int, input().split())    # 부분집합 원소의 수, 부분 집합의 합
    A = [i for i in range(1, 13)]
    # make subset
    subset = [[] * (1 << 12) for _ in range(1 << 12)]
    for i in range(1 << 12):
        for j in range(12):
            if i & (1 << j):
                subset[i].append(A[j])

    # find len(subset) = N
    N_list = []
    for i in range(1 << 12):
        if len(subset[i]) == N:
            N_list.append(subset[i])
    # print(N_list)

    # check sum = k
    cnt = 0
    for i in range(len(N_list)):
        if sum(N_list[i]) == k:
            cnt += 1
    # print(cnt)

    # check result
    result = 0
    if cnt > 0:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')

