# 최대 최소 찾기
arr = [1, 8, 4, 5, 6, 9, 1, 2, 7, 3]
m = len(arr)    # 배열의 개수

maxV = arr[0]   # 0번째 요소가 최댓값이라고 지정
for i in range(1, m):
    if maxV < arr[i]:   # 만약 다음 요소가 최댓값이라고 지정한 것보다 크다면
        maxV = arr[i]   # 최댓값을 더 큰 것으로 할당

print(maxV)