number = int(input()) # 스위치 개수 (100이하)
switch = list(input().split())  # 스위치 상태 1 켜짐 0 꺼짐
students = int(input()) # 학생 수
gender, switch_number1 = map(int, input().split()) # 학생 성별 남 1 여 2, 받은 수

if gender == 2:
    for order in switch:
        for i in range(len(switch)):
            
            

