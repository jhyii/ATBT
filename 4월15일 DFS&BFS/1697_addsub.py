import sys
from collections import deque #덱 이용
input = sys.stdin.readline #input 대체

"""
[숨바꼭질]
 x좌표 위에서 x-1, x+1, 2*x의 위치로 계속 이동하며 탐색
 가장 빠른 시간을 찾아야 하므로 주변 노드부터 탐색하는 풀이로 풀어서 k에 도달하면 바로 탐색 종료 (bfs)
"""
SIZE = 10**5 #수빈이와 동생의 점 최댓값

def bfs(n, k): #너비우선탐색
    time = [-1] * (SIZE + 1) #time배열 초기화
    que = deque() #덱 선언하기
    que.append(n) #덱에 수빈이의 위치 추가
    time[n] = 0 #time배열에서 수빈이의 위치 값 0으로 대입

    while que: #덱이 빌 때까지 반복
        curr = que.popleft() #덱의 가장 왼쪽 값을 지우면서 curr에 대입
        if curr == k: #만약 동생의 위치와 같다면
            return time[curr] #time배열의 요소 값 출력
        
        for next in (curr * 2, curr + 1, curr - 1): #순간이동할 경우와 걸을 경우 모두 탐색
            if next < 0 or next > SIZE or time[next] > -1: #next의 값이 0보다 작거나 최대위치보다 크거나 time에서 next인덱스인 값이 -1보다 클 때
                continue #넘어가기
            time[next] = time[curr] + 1 #아니면 time[next]에 time[curr]+1 대입
            que.append(next) #덱에 탐색할 위치 추가

# 입력
n, k = map(int, input().split()) #수빈이와 동생의 위치 입력받음
# 연산 + 출력
print(bfs(n, k)) #결과 출력