# 1. 간단한 N의 약수 (SWEA #1933)
   
#    - 반복, 출력(end=), 조건
#      입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.

N = int(input('수를 입력하세요: '))

for i in range(1, N+1):
    if N % i == 0:
        print(i, end = ' ')  # 가로로 공백을 두고 출력하자.



