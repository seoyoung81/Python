T = 10
for test_case in range(1, T + 1):
    m = int(input())
    infix = str(input())

    stack = []
    result = ''
    for token in infix:
        if token.isdecimal():   # token is number
            result += token
        else:                   # token is addition
            stack.append(token) # only addition

    while stack:
        result += stack.pop()


    for token in result:
        if token.isdecimal():
            stack.append(token)
        else:
            second = int(stack.pop())
            first = int(stack.pop())

            stack.append(first + second)

    print(*stack)


