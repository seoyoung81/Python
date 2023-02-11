# 버블 정렬
arr = [1, 2, 5, 3, 4, 2]
N = len(arr)

for i in range(N, 0, -1):
    for j in range(i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)