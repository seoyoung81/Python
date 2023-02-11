baby_gin_list = list(map(int, input())) # 667767
n = len(baby_gin_list)
cnt = [0] * 9

for i in range(n):
    cnt[baby_gin_list[i]] += 1
# print(cnt) // [0, 0, 0, 0, 0, 0, 3, 3, 0]
triplet = 0
run = 0
for i in range(9):
    if cnt[i] >= 3:
        triplet += 1
        cnt[i] -= 3
        continue
for i in range(7):
    if cnt[i] == 2 and cnt[i+1] == 2 and cnt[i+2] == 2:
        run += 2
        cnt[i] -= 2
        cnt[i+1] -= 2
        cnt[i+2] -= 2
        continue

    if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
        run += 1
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        continue

if triplet + run == 2:
    print('Baby-gin!')
else:
    print('You lose')