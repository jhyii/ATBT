import sys
input = sys.stdin.readline #입력시간 줄임

SIZE = 19 #바둑판 크기

"""
 [오목]

 1. 특정 좌표(r, c)를 가장 왼쪽으로 하는 가능한 모든 오목 배치에 대해 오목 여부 확인
    가능한 모든 배치 :  오른쪽, 아래, 우하향, 우상향
 2. (주의) 육목이상이 되는지 확인해야 함
"""

def promising(r, c, stone, board): #
    return 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == stone

def check_dir(r, c, d, board):
    stone = board[r][c] #현재위치의 돌

    # 가로, 세로, 우하향 대각선, 우상향 대각선
    dr = [0, 1, 1, -1] #0,1 가로 1,0세로
    dc = [1, 0, 1, 1] #1,1 우하향대각선 -1,1 우상향대각선

    if promising(r-dr[d], c-dc[d], stone, board): #규칙 확인
        return False #다 넘어갔다면 승부가 나지 않았음
    
    cnt = 0 # (r, c)를 가장 왼쪽으로 하는 이어지는 바둑알의 개수

    while cnt < 6 and promising(r, c, stone, board): #6보다 작고 규칙을 만족하면
        cnt += 1 #cnt 더하고
        r += dr[d] #위치 옮김
        c += dc[d] #위치 옮김
    
    return cnt == 5 #5개 이어졌으면 true

def is_end(r, c, board): #승부가 났는지
    # 가로, 세로, 우하향 대각선, 우상향 대각선
    for i in range(4):
        if check_dir(r, c, i, board): #i로 4개의 위치를 모두 탐색해서 True라면 
            return True #승부가 났음
    return False #숭부가 나지 않았음

def simulation(board): 
    for i in range(SIZE): #전체 탐색을 위한 반복문
        for j in range(SIZE): #전체 탐색을 위한 반복문
            # 돌이 없는 경우
            if not board[i][j]: #0이면
                continue #넘어감
            # 누군가 이겼으면
            if is_end(i, j, board): #이미 승자가 나왔으면
                return "{}\n{} {}".format(board[i][j], i+1, j+1) #승자와 가장 왼쪽 알의 위치 출력

    return 0 #승부가 결정되지 않음

# 입력
board = [list(map(int, input().split())) for _ in range(SIZE)] #바둑판 상태 입력
# 연산 + 출력
print(simulation(board)) #답 출력