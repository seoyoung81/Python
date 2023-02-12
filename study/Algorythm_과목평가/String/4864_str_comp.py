T = int(input())
for test_case in range(1, T+1):
    str1 = str(input())
    str2 = str(input())     # str2에 st1이 있는가?
    M = len(str1)
    N = len(str2)
    result = 0
    for i in range(N-M+1):
        if str1 == str2[i:i+M]:
            result += 1

    if result > 0:
        result = 1
    else:
        result = 0
    print(result)