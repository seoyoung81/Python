T = 10
for tc in range(1, T+1):
    N = int(input())    # 건물의 개수
    building_list = list(map(int, input().split())) # 건물의 높이 리스트로 받기

    result = 0
    m = len(building_list)
    for i in range(m-4):
        a, b, c, d, e = building_list[i], building_list[i+1], building_list[i+2], building_list[i+3], building_list[i+4]
        if max(building_list[i:i+5]) == c:
            second_max = max(a, b, d, e)
            result += c - second_max

    print(f'#{tc} {result}')
