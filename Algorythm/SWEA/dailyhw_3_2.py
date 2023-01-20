word = str(input()) # 문자열을 입력 받기
list_word = list(word) # 문자열을 알파벳으로 쪼갠 리스트로 만들기
# print(list_word)

n = len(list_word)   # 리스트 원소의 갯수 구하기
# print(n)

if n % 2 != 0:
    print(list_word[int((n-1)/2)])
else:
    print(list_word[int(n/2)-1:int(n/2)+1])

# 이 2개의 차이점은 뭘까?
# 윗 줄은 c 로 뜬다면 아랫줄은 ['c'] 로 뜬다