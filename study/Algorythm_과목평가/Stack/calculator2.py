T = 1
for test_case in range(1, T + 1):
    stack = []
    result = ''
    infix = str(input())    # 중위 표기법
    # 후위표기법으로 변경

    for token in infix:
        if token.isdecimal():   # token이 피연산자라면
            result += token
        else:                   # token이 연산자라면
            if not stack:       # empty stack
                stack.append(token) # stack push
            else:               # not empty stack
                if token == '*':    # 곱셈 연산자라면
                    while stack and stack[-1] != '+':
                        result += stack.pop()
                    stack.append(token)
                else:
                    while stack:
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()
    # 계산하기
    for token in result:
        if token.isdecimal():
            stack.append(token)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            if token == '+':
                stack.append(first + second)
            else:
                stack.append(first * second)

        print(stack)
