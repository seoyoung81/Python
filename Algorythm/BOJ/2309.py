height_list = []

for i in range(9):
    h = int(input())
    height_list.append(h)
# print(height_list) # [20, 7, 23, 19, 10, 15, 25, 8, 13]
sub = sum(height_list) - 100    # 40

# 2개 합 40 찾기 -> 36개
done = False
for first in height_list:
    for second in height_list[first+1:]:
        if first + second == sub:
            
            height_list.remove(first)
            height_list.remove(second)
            
    if done:
        break       
            
# print(height_list)
# new_height = ''.join([str(n) for n in height_list])

height_list.sort()

for h in height_list:
    print(h)




            

