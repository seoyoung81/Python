num = int(input())

num_list = []
for i in str(num):
    num_list.append(i)
# print(num_list)

sum = 0
for number in num_list:
    sum += int(number)

print(sum)

