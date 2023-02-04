def dict_list_sum(infos):
    age_sum = 0
    for info in infos:
        age_sum += info['age']
    return age_sum
print(dict_list_sum([{'name': 'kim', 'age': 12}, 
                    {'name': 'lee', 'age': 4}]))