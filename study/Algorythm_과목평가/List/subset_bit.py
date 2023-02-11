arr = [3, 6, 1, 5, 4]
n = len(arr)

for i in range(1<<n):   # 부분집합의 개수 1<<n
    for j in range(n):  # 원소의 수만큼 비트 계산
        if i & (1<<j):  # i의 j 번 비트가 1이라면 -> 부분집합에서 j번 이 채워져 있다면
            print(arr[j], end=', ')
    print()
print()