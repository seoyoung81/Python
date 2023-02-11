# 1
number = int(input())
for num in range(1, number+1):
#print(' ' * (number-num), '*' * num) # 오른쪽 정렬
    print(('*' * num).rjust(number))
