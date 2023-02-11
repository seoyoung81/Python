def binary_search(a, n, key):
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return middle
        elif a[middle] < key:    # 키 값 보다 중앙 값이 저 작으면
            start = middle + 1
        else:
            end = middle - 1
    return 'false'

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(a, 8, 6))