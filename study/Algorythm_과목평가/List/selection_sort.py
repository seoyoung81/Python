# 선택 정렬
'''
배열에서 최솟값을 찾아 첫번 째 값과 바꿔준다
'''
def selection_sort(arr, n):
    for i in range(n-1):    # 마지막 값은 어차피 제일 큰 값이여서 고려하지 않아도 됨
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 10, 22, 11], 5))