# 카운팅 정렬
arr = [0, 4, 1, 3, 1, 2, 4, 1]
k = max(arr)
cnt = [0] * (k+1)
sorted_list = [0] * len(arr)

for i in range(len(arr)):
    cnt[arr[i]] += 1

for i in range(1, len(cnt)):
    cnt[i] += cnt[i-1]

for i in range(len(arr)-1, -1, -1):
    cnt[arr[i]] -= 1
    sorted_list[cnt[arr[i]]] = arr[i]

print(sorted_list)


# k = max(arr)
# cnt = [0] * (k+1)
# sorted_arr = [0] * (len(arr))
#
# for i in range(len(arr)):
#     cnt[arr[i]] += 1    # 개수 세기
#
# for i in range(1, len(cnt)):
#     cnt[i] += cnt[i-1]  # 개수 누적 시키기
#
# for i in range(len(arr)-1, -1, -1):    # 뒤에서부터
#     cnt[arr[i]] -= 1    # 하나씩 빼고
#     sorted_arr[cnt[arr[i]]] = arr[i]    # 할당하기
#
# print(sorted_arr)

'''
def CountingSort(data, temp, counts):
    # data : 입력 원본 배열, temp : 정렬된 배열, counts : 카운트 배열
    counts = [0] * (k + 1) # k : 원소 종류의 개수
    
    # 카운트 배열 만들기
    for i in range(0, len(A)):
        counts[data[i]] += 1
        
    # 카운트 배열 누적합으로 바꾸기
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
        
    # 정렬하기
    for i in range(0, len(data)):
        counts[data[i]] -= 1
        temp[ counts[data[i]] ] = data[i]
        
'''