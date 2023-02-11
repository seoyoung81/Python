# 3. Dictionary로 이루어진 List의 합 구하기
   
#    * Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.
     
#      ```python
#      dict_list_sum([{'name': 'kim', 'age': 12}, 
#                     {'name': 'lee', 'age': 4}]) #=> 16

dict_list = ([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])

def dict_list_sum(dict_list):
    m = len(dict_list) # 리스트 안에 있는 딕셔너리의 갯수

    age_sum = 0
    for i in range(m):
        age_sum += dict_list[i]['age']
    return age_sum

print(dict_list_sum(dict_list))


def dict_list_sum(dict_list):
        age_sum = 0
        for age in dict_list:
            age_sum += age['age']       # 어떤거의 어떤건지 잘 보자. 리스트인지 딕셔너리의 value 값인지 키 값인짙ㄴ
        return age_sum