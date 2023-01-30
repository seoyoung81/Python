chulsu = [[0]*5 for _ in range(5)]  # 0 으로 된 이차원 리스트. 숫자가 불리면 1로 바꾸기
# print(chulsu)

bingo_list = []
for i in range(5):
    a = list(map(int, input().split()))     # a를 5줄 입력받고
    bingo_list.append(a)                    # 5X5 2차원리스트 생성
# print(bingo_list)

turn = 0                                    # 횟수 0
mc_list = []
for p in range(5):
    b = list(map(int, input().split()))     # b를 5줄 입력받고
    mc_list.append(b)                       # 5X5 2차원리스트 생성
    for q in range(5):                      # 
        turn += 1
# print(mc_list)

        for j in range(5):
            for p in range(5):  
                for q in range(5):
                    if mc_list[i][j] == bingo_list[p][q]:
                        chulsu[p][q] = 1

                        bingo = 0
                        if sum(chulsu[p]) == 5:
                            bingo += 1
                        if sum(k[p] for k in chulsu) == 5:
                            bingo += 1
                        
                        if chulsu[0][4] + chulsu[1][3] + chulsu[2][3] + chulsu[3][2] + chulsu[4][0] == 5:
                            bingo += 1
                            
                        if chulsu[0][0] + chulsu[1][1] + chulsu[2][2] + chulsu[3][3] + chulsu[4][4] == 5:
                            bingo += 1
                            
                        if bingo >= 3:
                            print(turn)
                        
                        print(bingo)

