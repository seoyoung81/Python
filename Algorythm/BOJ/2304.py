N = int(input())    # 기둥의 개수

a_list = []
for _ in range(N):
    x, y = map(int, input().split())     # y: 높이, x: x좌표
    a_list.append([x,y])                 # x, y 를 이차원 리스트에 배정함   

b_list = sorted(a_list)
# print(b_list)  # x를 기준으로 정렬

max_list = []
for i in range(len(b_list)):
    max_list.append(b_list[i][1])         # y 값 중 가장 큰 값을 찾자
# print(max_list)  

max = max(max_list)  # 높이가 가장 큰 값 (여기를 기준으로 왼쪽 오른쪽을 보자)
# print(max)

for i in range(0, max):
    if b_list[i][1] >= b_list[i+1][1]:

        b_list.pop(i+1)
# print(b_list)