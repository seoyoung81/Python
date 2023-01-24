n = 1
slst, swlst = [], [] # 소금의 농도, 소금물의 양
while n <= 5:
    sl = input('소금물의 농도를 입력하세요. :')
    sw = input('소금물의 양을 입력하세요. :')
    if sl == str('done'):
        break
    else:
        slst.append(sl)
        swlst.append(sw)
    n += 1


salt_water = round(int((sum(swlst), 2)))
density = round(int(sum(slst) * 100 / sum(swlst), 2))

print(f'소금물의 양은 {salt_water}, 소금물의 농도는 {density}입니다.')







# 총 소금물의 양 5개 더한것
# 총 소금의 양: a * b / 100  5개 더한 것
# 총 퍼센트 농도: 총 소금의 양 / 총 소금물의 양 * 100