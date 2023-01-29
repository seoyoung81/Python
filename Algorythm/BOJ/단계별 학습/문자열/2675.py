T = int(input())    # 테스트 케이스 개수

for _ in range(T):
    R, S = input().split()

    
    for i in S:
        print(i * int(R), end = '')
    print()     # 다음 줄에 입력가능하게 하기