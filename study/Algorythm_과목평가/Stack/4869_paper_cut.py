T = int(input())    # test_case
for test_case in range(1, T + 1):
    N = int(input())
    n = N // 10

    memo = [0] * (n + 1)
    memo[0] = memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + 2 * memo[i-2]

    print(f'#{test_case}', memo[n])