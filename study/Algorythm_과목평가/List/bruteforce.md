```python
text = "SSAFY 09 Let's go~!"  # 전체 텍스트 // target
pattern = "go"  # 찾을 패턴

def BruteForce(pattern, text):
    N = len(text)  # 전체 텍스트의 길이
    M = len(pattern)  # 찾을 패턴의 길이
    i = 0  # text 의 인덱스
    j = 0  # pattern 의 인덱스

    while j < M and i < N:

        # 틀린 곳을 발견했다면 index의 위치를 초기화 
        if text[i] != pattern[j]:
            # 지금 위치에서 j만큼 온 상태에서 틀린곳이 발견됨, 
    		# 지금위치 - j + 1을 하면 다음 위치가 됨. 아래에서 1을 더해주므로 (i - j)
            i = i - j

            # j(pattern)는 0부터 다시 시작하므로 -1로 변경 후 아래에서 1을 더해서 0으로
            j = - 1
        i = i + 1
        j = j + 1

    if j == M:
        return i - M  # 검색 성공
    else:
        return -1  # 검색 실패

print(BruteForce(pattern, text))
```

```python
# 심플 버전

text = "SSAFY 09 Let's go~!"  # 전체 텍스트 
pattern = "Le"  # 찾을 패턴

def BruteForce(pattern, text):

    # text를 처음부터 끝까지 순회(단, pattern의 길이만큼)
    for idx in range(len(text) - len(pattern) + 1):
        # pattern을 처음부터 끝까지 순회
        for j in range(len(pattern)):
            # 다르면 break
            if text[idx+j] != pattern[j]:
                break
        # 다른게 없다면 정답, idx(시작점) return
        else:
            return idx
    else:
        return -1

print(BruteForce(pattern, text))
```

* KMP
  
```python
# T : target / P : pattern

def pre_process(T):
    lps = [0] * len(T)

    # lps를 만들기 위한 prefix에 대한 idx,
    j = 0
    
    """
    i : pattern에서 지나가고 있는 id
    j : 지나가고 있는 idx와 pattern의 앞부분과 같은 부분에 대한 idx
    """

    # 처음부터 끝까지 순회를 돌면서
    for i in range(1, len(T)):
        # i 와 j가 같으면 lps의 i 자리에 j+1을 넣어줍니다. 
        #(prefix idx 위치에 있는 char와 같으면 lps에 숫자 추가)
        if T[i] == T[j]:
            lps[i] = j + 1
            j += 1
        # 다르다면, j를 초기화 해주어 pattern의 가장 처음부터 인식하자.
        # 그 자리에서 기존의 j자리(비교를 하고 있던 자리)가 아닌 pattern 처음으로 돌아가 비교.
        else:
            j = 0
            if T[i] == T[j]:
                lps[i] = j + 1
                j += 1

    return lps

T = 'abcdabeeababcdabcef'
P = 'eaba'

lps = pre_process(T)
print(lps)
```

```python
def KMP(T, P):

    lps = pre_process(T)

    # i : text를 순회하는 index
    i = 0
    # j : pattern을 순회하는 index
    j = 0

    position = -1
    while i < len(T):
        # 같으면 이동
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            # 다른데 j가 0이 아니라면, i의 자리는 유지한 채 j만 이동 후 비교 시작
            if j != 0:
                j = lps[j - 1]
            # 다른데 j가 0이라면, i를 한칸만 이동하여 처음부터 진행 하듯이 진행
            else:
                i += 1
        # j가 pattern을 다 순회하면 성공
        if j == len(P):
            position = i - j
            break

    return position

T = 'abcdabeeababcdabcef'
P = 'eaba'

position = KMP(T, P)
print(position)
```

```python
def pre_process(P, M, PI):
    i, j = 0, -1
    PI[0] = -1
    while i < M:
        while j > -1 and P[i] != P[j]:
            j = PI[j]
        i += 1
        j += 1
        PI[i] = j

def KMP(T, N, P, M, PI):
    i, j = 0, 0
    pos = -1
    while i < N:
        while j >= 0 and T[i] != P[j]:
            j = PI[j]
        i += 1
        j += 1
        if j == M :
            pos = i - j
            break
    return pos

T = 'abcdabcdabcdabcef'
P = 'abcdabcef'
PI = [0] * (len(P) + 1)

N = len(T)
M = len(P)
pre_process(P, M, PI)
pos = KMP(T, N, P, M, PI)
print(pos)
```
