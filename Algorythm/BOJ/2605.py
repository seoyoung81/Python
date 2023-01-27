students = int(input()) # 학생 수
number_list = list(map(int, input().split()))   # 줄은 선 차례대로 뽑은 번호

# list 에서 index[i] 는 0 ~ i 까지 뽑을 수 있음

student_list = []   # 최종적으로 줄을 선 순서를 담을 빈 리스트

for i in range(len(number_list)):
    student_list.insert((i-number_list[i]), (i+1))
    # print((i-number_list[i]))


# # i= 0 일 때 1번 선수는 그냥 0
# student_list.insert(0,1)

# # i = 1 일 때 2번 선수가 1을 뽑았다면
# student_list.insert(1-1, 2)    
result = ' '.join([str(n) for n in student_list])
print(result)

    