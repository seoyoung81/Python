orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order_list = orders.split(',')

ice_list = []
for order in order_list:
    if '아이스' in order:
        ice_list.append(order)
# print(ice_list)
ice_orders = len(ice_list)
print(f'총 {ice_orders}잔의 아이스 음료 주문이 들어왔습니다.')

# list에서 요소가 각 몇 개 인지 세기
# try, except 문 사용
count = {}  #count는 빈 딕셔너리
for i in order_list:    # order_list에 있는 i가
    try:
        count[i] += 1   # 개수에 따라 1개 증가
    except:     # 예외
        count[i] = 1    # 갯수가 1개인 경우는 예외
print(count)
