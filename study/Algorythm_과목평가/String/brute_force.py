# p = ' is'    # 찾고 싶은 패턴
# t = 'This is a book'    # 찾을 패턴
# M = len(p)
# N = len(t)
#
# def BruteForce(p, t):
#     for i in range(N-M+1):
#         for j in range(M):
#             if t[i+j] != p[j]:
#                 break
#         else:
#             return i
#     return -1
#
# print(BruteForce(p, t))
#
# 전체 문장에서 찾고 싶은 패턴이 몇 개?

p = 'ab'
t = 'ababab'
M = len(p)
N = len(t)

def brute_force(p, t):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
    return cnt
print(brute_force(p, t))