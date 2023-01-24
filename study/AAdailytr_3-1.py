# 못 풀었다 !!!!!

fruits = str(input())
fruits_lower = fruits.lower()
# print(fruits_lower) 소문자로 바꾸기

fruits_list = fruits_lower.split(',')
print(fruits_list) #문자열을 리스트로 만들기

fresh = fruits_list
for char in fruits_list:
    for i in fresh:
        if 'rotten' in fresh:
            fresh[i] = fresh[i].replace(char, '')
print(fresh)
#         result = result.replace(char, '')
# print(result)

# char = 'rotten'
# for i in fruits_lower:
#     fruits_lower = fruits_lower.replace(char[i], '')
# print(fruits_lower)










# apple,rottenBanana,apple,RoTTenorange,Orange