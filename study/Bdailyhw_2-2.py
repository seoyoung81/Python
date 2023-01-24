orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order_list = orders.split(',')
# print(len(order_list))

count = 0
for order in order_list:
    if '아이스' in order:
        count += 1
# print(count)
print(f'아이스 음료 주문은 {count}잔 입니다.')   

# new_list = {}
# for order in order_list:
#     try:
#         new_list[order] += 1
#     except:
#         new_list[order] = 1
# print(new_list)

new_list = {}
for order in order_list:
    try:
        new_list[order] += 1
    except:
        new_list[order] = 1
print(new_list)

