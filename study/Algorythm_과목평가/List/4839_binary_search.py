# binary Search
'''
배열 인덱스의 이진탐색과
숫자들의 이진탐색은 다름
'''
def binary_search(n, a):    # make binary_search function
    start = 1
    end = n
    i = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == a:
            return i
        elif middle > a:
            i += 1
            end = middle
        elif middle < a:
            i += 1
            start = middle

# print(binary_search(400, 300))
# print(binary_search(400, 350))

T = int(input())    # testcase
for test_case in range(1, T+1):
    book, A, B = map(int, input().split())  # page, a가 찾고 싶은 페이지, b가 찾고 싶은 페이지
    a_count = binary_search(book, A)
    b_count = binary_search(book, B)

    if a_count < b_count:
        print(f'#{test_case} A')
    elif a_count == b_count:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} B')


