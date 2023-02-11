T = int(input())    # test_case
for test_case in range(1, T+1):
    set_list = list(map(int, input().split()))  # set_list input
    # subset
    m = len(set_list)   # 원소의 개수
    subset = [[] * (1 << m) for _ in range(1 << m)]
    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                subset[i].append(set_list[j])

    # sum = 0
    cnt = -1    # empty set
    for i in range(1 << m):
        total = 0
        m = len(subset[i])
        for j in range(m):
            total += subset[i][j]
            if total == 0:
                cnt += 1

    # 존재하는가?
    if cnt > 0:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
