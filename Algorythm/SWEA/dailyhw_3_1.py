fruits = input().lower() # 문자열 소문자로 바꿔주기
# print(fruits)

fruits_list = list(fruits.split(',')) # 문자열을 쉼표를 기준으로 리스트로 만들기
# print(fruits_list)

for fruit in fruits_list:   # fruits_list 에 있는 fruit 에 대해서
    if "rotten" in fruit:   # 만약 단어에 rotten이 포함되어 있으면
        fruits_list.remove(fruit)   # 리스트에서 그 단어를 제거하자

print(fruits_list)
