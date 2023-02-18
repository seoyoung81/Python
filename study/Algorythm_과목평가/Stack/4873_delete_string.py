T = int(input())
for test_case in range(1, T + 1):
    string = str(input())

    stack = []
    for alpha in string:
        if not stack: # stack is empty
            stack.append(alpha)
        else:   # not empty
            if stack[-1] == alpha:  # 문자열이 중복이면
                stack.pop()         # 삭제
            else:                   # 중복이 아니라면
                stack.append(alpha) # 추가

    print(f'#{test_case} {len(stack)}')
