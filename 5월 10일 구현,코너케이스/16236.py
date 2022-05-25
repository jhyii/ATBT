import sys
from collections import deque #덱 이용
input = sys.stdin.readline #인풋시간줄임

INF = 401 #공간의 크기가 20*20이라서 최대값 401

"""
 [아기 상어]

 1. 상어로부터 가장 가까운 거리에 있는 모든 물고기 탐색 (BFS)
 2. 우선순위 조건에 맞추어 먹으러 갈 물고기 확정
    탐색하는 방향에 우선순위를 두는 걸로 해결되지 않음! (예제 입력 4) 정렬 필요
 3. 상어가 이동할 수 있는 곳이 없을 때까지 BFS 탐색 반복

 입력 범위가 작기 때문에 매번 BFS 탐색을 반복해도 시간 초과 X
 가능한 물고기의 최대 마리 수 : 399마리
 최대 BFS 탐색 횟수 : 399회, 1회 탐색마다 while 문은 최대 400회 미만으로 순회
 총 연산 횟수 약 160000번으로 충분히 가능

 해설 : https://myunji.tistory.com/378
 *글 자체는 별로 도움이 안되고...그냥 리팩토링하면 코드가 이렇게 되는구나 정도만 봐주세요
"""

def next_pos(n, shark_size, shark, board): #다음 위치 탐색하는 함수
    dr = [-1, 1, 0, 0] #row이동
    dc = [0, 0, -1, 1] #colum이동

    min_dist = INF #최솟값 초기화
    que = deque()   # 상어가 갈 수 있는 곳
    dist = [[0]*n for _ in range(n)]     # 상어로부터의 거리 - 초기값은 0으로
    pos_list = []    # 상어가 먹을 수 있는 물고기들의 위치

    dist[shark[0]][shark[1]] = 1 #상어가 있는 위치의 dist를 1로
    que.append(shark) #덱에 append

    while que: #큐에 요소가 남아있을 때까지
        row, col = que.popleft() #탐색할 물고기의 위치

        # 최단거리 이상은 탐색할 필요 없음
        if dist[row][col] >= min_dist: #현재 물고기와의 거리가 최단거리가 아니면
            continue #아래 실행 안함

        for i in range(4): #최단거리라면 실행
            nr = row + dr[i] #주변 모든 물고기 탐색
            nc = col + dc[i] #주변 모든 물고기 탐색
            if not (0 <= nr < n and 0 <= nc < n) or dist[nr][nc] or board[nr][nc] > shark_size: #설정한 위치가 공간을 넘어가거나 dist가 0이거나 물고기가 아기상어보다 크면 
                continue #진행할 수 없음

            dist[nr][nc] = dist[row][col] + 1 #움직인 거리 재설정
            
            # 먹을 수 있는 물고기 발견
            if board[nr][nc] and board[nr][nc] < shark_size: #물고기가 있고, 상어보다 작다면
                pos_list.append((nr, nc)) #먹을 수 있는 물고기 위치에 추가
                min_dist = dist[nr][nc] #최단거리에 현재거리 대입
                continue #넘어감
            
            que.append((nr, nc)) #덱에 추가

    # 상어가 갈 수 있는 곳이 없음
    if not pos_list: #pos_list에 값이 없다면
        return min_dist, (-1, -1) #최단거리와 (-1,-1)리턴해서 갈 수 있는 곳이 없음을 표기

    pos_list.sort() #pos_list 정렬

    return min_dist - 1, pos_list[0] #탐색이 끝나면 최단 거리에서 1뻬고, 가장 가까운 pos와 함께 출력

def simulation(n, shark, board):
    ans = cnt = 0 #카운트 초기화
    size = 2 #아기상어 크기

    while True: #먹을 수 있는 물고기 있을 때까지
        dist, pos = next_pos(n, size, shark, board) #다음 물고기의 위치
        # 더 이상 먹을 수 있는 물고기가 공간에 없음
        if dist == INF: #초기값으로 설정되어 있다면
            break #반복종료
        
        ans += dist #정답에 거리 더함
        cnt += 1 #먹은 횟수 증가
        
        # 상어 크기 증가
        if cnt == size: #먹은 횟수가 상어크기랑 같다면
            cnt = 0 #cnt 다시 0으로
            size += 1 #상어 크기 1커짐

        # 상어 이동
        board[shark[0]][shark[1]] = 0 #탐색한 곳은 0으로 바꿔줌
        shark = pos #이동한 위치로 상어위치 바꾸기

    return ans #답 출력

# 입력
n = int(input()) #공간의 크기 입력
board = [list(map(int, input().split())) for _ in range(n)] #공간의 상태

for i in range(n): #아기상어 위치탐색 위한 반복문
    for j in range(n): #모든 공간 탐색
        if board[i][j] == 9: #아기상어 위치는 9
            shark_pos = (i, j) #튜플로 저장
            break

print(simulation(n, shark_pos, board)) #정답 출력