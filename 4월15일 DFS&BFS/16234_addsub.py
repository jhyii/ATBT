import sys #sys임포트
from collections import deque #덱 사용
input = sys.stdin.readline #실행시간 줄여줌

"""
[인구이동]
0. 인구이동이 일어날 수 있는 나라(처음에는 모든 나라)의 좌표를 좌표 큐에 저장
1. bfs 탐색을 통해 연합을 확인하고, 연합에 포함된 나라의 인구이동을 진행한다.
2. 인구 이동이 있었던 나라는 다음 날에도 인구이동이 시작될 수 있으므로 좌표 큐에 다시 넣어준다.
    -> 직전 이동이 있었던 나라에 대해서만 bfs 탐색 진행
    - 인구 이동이 일어나지 않은 두 나라 사이에서는 다음 날에도 인구이동이 일어날 수 없음
3. 인구이동이 전혀 일어나지 않을 때까지 반복
"""

def bfs(n, left, right, i, j, day): #너비우선탐색진행하는 함수
    dr = [-1, 1, 0, 0] #이동할 방향 배열
    dc = [0, 0, -1, 1] #이동할 방향 배열

    que = deque() #너비우선탐색은 덱으로 구현
    que.append((i, j)) #덱에 (i,j)를 추가
    total = 0   # 연합의 인구 수 합계
    count = 0   # 연합에 포함된 나라의 수
    cord = []   # 연합에 포함된 나라의 좌표
    
    while que: #덱이 비면 종료
        r, c = que.popleft() #덱의 가장 왼쪽 원소들을 지우면서 r,c에 저장
        count += 1 #count 증가
        total += board[r][c] #각 나라의 인구 수 합계
        cord.append((r, c)) #(r,c)는 나라의 좌표

        for x in range(4): #dr,dc의 len
            new_r = r + dr[x] #new_r은 원래 좌표 r에 dr의 인덱스 x인 값이 더해짐. 좌우로 이동해서
            new_c = c + dc[x] #new_c은 원래 좌표 c에 dc의 인덱스 x인 값이 더해짐. 위아래로 이동해서
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c] == day: #new_r이나 new_c가 n보다 커지거나 이 나라의 방문 여부가 day와 같다면 계속진행
                continue

            # 이 때 여기서 visited에 표기를 하면 안됨
            # 현재는 조건에 맞지 않지만, 이후에 연합에 있는 다른 나라에 의해 연합에 들어올 수 있음

            if left <= abs(board[new_r][new_c] - board[r][c]) <= right: #새로운 국가의 인구수에서 원래 인구수를 뺀 값이 left와 right사이일 때
                que.append((new_r, new_c)) #덱에 새로운 국가를 추가
                visited[new_r][new_c] = day #새로운 나라 방문여부는 day로 바꾸기

    # 적어도 나라 2개 이상이 모여야 연합을 이루었다고 볼 수 있음
    if count > 1: #연합 수가 1개보다 많다면
        avg = total // count #인구평균은 전체 인구수를 나라 수로 나눔
        # 인구 이동
        for r, c in cord: #인구 이동할 나라들
            board[r][c] = avg #이 나라들 인구는 인구평균이 됨
            # 인구의 이동이 있는 나라는 다음 이동이 시작될 가능성이 있음
            countries.append((r, c)) #이 나라 추가
    
    return count > 1 #count값에 따른 bool 반환

def simulation(n, left, right): #day세는 함수
    day = 0 #날짜세는변수
    while True:
        size = len(countries)   # 이번에 탐색할 수 있는 나라의 수
        flag = False #연합 이루었는지 확인하는 변수, False로 초기화
        day += 1 #날짜 하루 추가
        for _ in range(size): #나라 수만큼 반복함
            i, j = countries.popleft() #countries의 가장 왼쪽 값을 지우며 i,j에 저장
            if visited[i][j] == day: #i,j나라의 방문여부가 day와 같다면
                continue #계속 진행
            visited[i][j] = day #i,j나라 방문 여부에 day 들어감
            if bfs(n, left, right, i, j, day):   # bfs 결과 true면 연합을 이루었다는 의미이므로 flag 표시
                flag = True

        if not flag: #flag가 false일 때
            return day - 1 #day-1값을 리턴

# 입력
n, left, right = map(int, input().split()) #순서대로 나라 수, 땅 크기 입력받음
board = [list(map(int, input().split())) for _ in range(n)] #각 나라의 인구수를 입력받아 배열에 저장

# 방문배열
visited = [[0]*n for _ in range(n)] #방문여부 저장할 배열, n개만큼 0으로 초기화
# 나라
countries = deque([(i, j) for i in range(n) for j in range(n)]) #나라의 좌표 생성

# 연산 + 출력
print(simulation(n, left, right)) #결과 출력