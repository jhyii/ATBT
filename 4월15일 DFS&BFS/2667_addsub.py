import sys
from collections import deque #덱을 이용
input = sys.stdin.readline #input대체

"""
[단지 번호 붙이기] - bfs

- 단순 탐색
- (주의) 단지 내 집의 수를 "오름차순"으로 출력

- 이 풀이에서는 방문체크 배열을 따로 사용하지 않고, 처음 지도에 표기를 1 -> 0으로 바꾸어 중복으로 탐색하지 않도록 함
"""

def bfs(i, j, n, matrix): #너비우선탐색
    dr = [-1, 1, 0, 0] #이동방향 배열
    dc = [0, 0, -1, 1] #이동방향 배열

    que = deque() #덱 선언
    que.append((i, j)) #덱에 i,j 추가
    count = 1 #집 하나 있으면 일단 단지 +1임

    while que: #덱이 비기 전까지 반복
        r, c = que.popleft() #덱의 가장 왼쪽 값들을 r,c에 저장하면서 지우기
        for x in range(4): #이동방향 배열의 len
            new_r = r + dr[x] #새로운 좌표는 r에 dr의 x번째 요소만큼 이동한 것
            new_c = c + dc[x] #새로운 좌표는 c에 dc의 x번째 요소만큼 이동한 것
            # 새 좌표가 범위에 맞지 않거나, matrix에 0으로 표기되어 있으면 건너 뜀
            if not (0 <= new_r < n and 0 <= new_c < n) or not matrix[new_r][new_c]:
                continue #건너뛰기
            matrix[new_r][new_c] = 0 #새로운 좌표 탐색했으니까 0으로 바꿔줌
            que.append((new_r, new_c)) #덱에 새로운 좌표 추가
            count += 1 #카운트 +1

    return count #카운트 출력

# 입력
n = int(input()) #지도의 크기 입력받음
matrix = [list(map(int, input().rstrip())) for _ in range(n)] #n*n배열로 집의 분포 입력받음

apartment = []  # 단지 수 저장할 리스트

for i in range(n): #row
    for j in range(n): #column
        if not matrix[i][j]: #지도에서 i,j좌표 0이면
            continue #넘어감
        matrix[i][j] = 0 #i,j에 0 대입
        apartment.append(bfs(i, j, n, matrix)) #탐색결과를 단지수 저장하는 리스트에 추가

apartment.sort()    # 정렬

# 출력
print(len(apartment)) #총 단지 수 출력
print(*apartment, sep='\n') #단지내 집 수 출력