# number = int(input())

# for i in range(1, number+1):
#     print(i)


# for j in range(1, number):        # 가로로 출력하기 
#     print(j, end = ' ')

# for k in range(number+1, 0, -1):
#     print(k)

# for l in range(number, -1, -1):
#     print(l, end = ' ')

# # 1부터 n 까지의 합 구하기
# num = int(input())
# sum = 0
# for a in range(num+1):
#     sum += a
# print(sum)

# number = int(input())
# for b in range(1, number+1):
#     print(('*' * b).rjust(number))

# 중간값 찾기
mid_list = list(input().split())
# print(mid_list)
m = len(mid_list)

rmid_list = sorted(mid_list)
midnum = rmid_list[int((m)/2)]
print(midnum)