def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    global queue
    front += 1
    queue_temp = queue[:]
    queue = queue[1:]
    return queue_temp[front]

T = int(input())    # test case
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N개의 숫자로 이루어진 수열에서 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번
    numbers = list(map(int, input().split()))   # N개의 숫자들
    queue = [0] * (M + M + 1)
    front = -1  # 시작은 -1
    rear = -1

    for i in range(N):
        enqueue(numbers[i])     # numbers 값 추가


    j = 0
    while j != M-1: # M번 미루겠다
        m = j % N   # m은 numbers의 인덱스 조절을 위해 j를 N으로 나눈 나머지로 정한다
        rear -= 1   # 바로 뒤에 추가하고 싶으니까 rear 값을 하나씩 땡겨야됨
        enqueue(numbers[m]) # m번째 요소 뒤에 추가
        dequeue()   # 맨 앞 요소 제거
        j += 1      # 다음 계속 반복



    print(f'#{test_case}', queue[0])

