infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

# age_infos = []
# for dic in infos:
#     age_infos.append([dic].values())
# print(age_infos)

age_list = list(i['age'] for i in infos)
# print(age_list)

sum = 0
for i in range(len(age_list)):
    sum += age_list[i]
print(sum)