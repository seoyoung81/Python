A, B = map(str, input().split())

reverse_A = int(A[::-1])
reverse_B = int(B[::-1])

# print(reverse_A)

if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)


