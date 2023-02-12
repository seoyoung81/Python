T = int(input())    # testcase
for test_case in range(1, T+1):
    sentence, word = map(str, input().split())
    M = len(word)
    N = len(sentence)

    # 같은 단어 몇 개인지 찾기 (한 번 찾아진 단어는 다시 찾으면 안됨)
    i = 0
    cnt = 0
    while i < N-M+1:
        for j in range(M):
            if sentence[i+j] != word[j]:
                continue
        else:
            i = i + M + 1
            cnt += 1

    # 타이핑 횟수 세기
    result = N - cnt * (M - 1)
    print(f'#{test_case} {result}')
