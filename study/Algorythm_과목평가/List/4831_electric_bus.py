T = int(input())
for tc in range(1, T+1):
    max_movement, bus_station, charger_station = map(int, input().split())
    # 최대 이동 정류장 수, 총 정류장 수, 충전기가 설치된 정류장
    station = [int(i) for _ in range(bus_station)]
    print(station)
    chargers = list(map(int, input().split()))

    # 아예 실패인 경우
    for i in range(bus_station-max_movement+1):
        for j in range(i, i+max_movement):
            if bus_station[j] not in chargers:
                print(0)

    # 최소 충전 횟수 구하기
