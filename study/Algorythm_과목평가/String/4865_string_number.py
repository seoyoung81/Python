T = int(input())
for test_case in range(1, T+1):
    str1 = str(input()) # 짧은거
    str2 = str(input())
    M = len(str1)
    N = len(str2)
    cnt_list = [0] * M
    # 문자가 각 몇 개 있는지 세주기
    for i in range(N):
        for j in range(M):
            if str1[j] == str2[i]:
                cnt_list[j] += 1
    # print(cnt_list)
    print(max(cnt_list))