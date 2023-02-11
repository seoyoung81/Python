T = int(input())    # 테스트 케이스의 개수

for tc in range(1, T+1):
    N = int(input())    # 카드 장수
    numbers = sorted(list(map(int, input())))

    # 숫자 몇개인지 세주기
    cnt = [0] * 10
    for i in range(len(numbers)):
        cnt[numbers[i]] += 1

    # print(cnt)
    # 최댓값 구하기
    maxV = max(cnt)
    # 가장 많은 카드의 번호
    for i in range(len(cnt)-1, -1, -1):
        if cnt[i] == maxV:
            card_number = i
            break

    print(f'#{tc} {card_number} {maxV}')