words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 애너그램 단위로 그룹핑하기
# 함수 사용하기

def anagram(words):
    anagrams = {}       # 빈 딕셔너리 생성

    for word in words:      # words 에 있는 단어 반복
        key = ''.join(sorted(word))     # key는 정렬한 단어의 문자열
        # print(key)
        anagrams.setdefault(key, [])    # setdefault(key값, default값) -> 사전 처리
        anagrams[key].append(word)      # anagrams[key] 의 value 값으로 word를 추가한다
    list(anagrams.values())             # anagrams의 values 값을 리스트로 형 변환 해준다

    return anagrams

print(anagram(words))


