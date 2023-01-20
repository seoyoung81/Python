infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

#print(list(m['age'] for m in infos)) # 딕셔너리 안에 있는 리스트의 value 값 출력
infos_list = list(m['age'] for m in infos)

sum = 0
for i in range(len(infos_list)):
    sum += infos_list[i]

print(sum)