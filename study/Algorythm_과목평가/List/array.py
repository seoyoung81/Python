arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 행 우선 순회
n = len(arr)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')

# 열 우선 순회
for j in range(n):
    for i in range(n):
        print(arr[i][j], end=' ')

# 지그재그 순회
for i in range(n):
    for j in range(n):
        print(arr[i][j + (n-1-2*j)*(i%2)]) # 홀인 경우에만 뒤에서 옴

# 전치행렬
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)