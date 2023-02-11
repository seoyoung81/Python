# 일렬로 되어 있는 자료를 순서대로 검색하는 방법
# 정렬되어 있지 않은 경우
arr = [1,3,2,5,4,6,8,7,9]
def sequential_search(a, n, key):
  i = 0
  while i < n and a[i] != key:
      i += 1
  if i < n:
      return i
  else:
      return -1

print(sequential_search(arr, len(arr), 8))

# 정렬 되어 있는 경우
def sequential_search_2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1

print(sequential_search_2([1,2,3,4,5], 5, 3))