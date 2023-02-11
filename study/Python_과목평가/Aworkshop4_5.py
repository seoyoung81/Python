# 5. 숫자의 의미
   
#    * 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 
# get_secret_word 함수를 작성하시오. 
#      단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

# chr(number) => 정수를 아스키 코드 문자로 반환

num_list = list(map(int, input().split()))

def get_secret_word(num_list):
    word = ''
    for number in num_list:
        word += chr(number)     # 문자열을 추가해서 출력하고 싶은경우 빈 문자열에 더해주면 된다
    return word

print(get_secret_word(num_list))






