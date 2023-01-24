password = ''

chance = 1

while password != '0124' and chance <= 3:

    password = str(input('비밀번호를 입력하세요 :'))
    chance += 1

if chance > 3:
    print('비밀번호를 3회 이상 틀렸습니다.')
else:
    print('비밀번호가 맞습니다.')

