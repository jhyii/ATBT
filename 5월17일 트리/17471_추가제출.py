import sys
input = sys.stdin.readline #입력속도 위해서

INF = 10**3 #최대로 설정
ans = INF #정답 초기화

"""
 [게리맨더링]

 1. 구역을 나누는 모든 경우의 수 구하기 - 백트래킹
 - 두 선거구로 나누는 경우이므로 모든 구역에 대해 true/false로 구분해서 경우의 수 구하기
 - 이때, 중복 연산 피하기 위해 1번 구역은 true로 고정. (집합끼리 구분할 필요가 없으므로 1번이 false일 때의 경우의 수는 1번이 true일 때와 정확히 일치)
 2. 각 경우마다 나눈 두 구역이 조건(구역 내 정점이 모두 연결)을 만족하는지 확인 - dfs
 - 구역 내 한 정점에서 dfs 탐색을 시작해서 구역 내의 모든 정점을 방문했다면 조건 만족한 것임
 3. 두 구역이 조건을 만족한다면 인구 수의 차이 구해서 최솟값 갱신
"""

# 두 선거구의 인구 수 차이 구하는 함수
def calc_diff():
    sum1 = sum2 = 0 #0으로 초기화
    for i in range(1, n+1): #1에서 n까지 반복
        if is_ward[i]: #True일 때
            sum1 += people[i] #sum1에 더해줌
        else: #false일 때
            sum2 += people[i] #sum2에 더해줌

    return abs(sum1 - sum2) #인구수차이 출력

# 선거구 내의 정점 연결됐는지 탐색하는 dfs 함수
def dfs(curr, state): 
    if visited[curr]: #True라면
        return 0 #0리턴

    visited[curr] = True #True로 갱신해줌
    cnt = 1 #cnt 1로 초기화
    for next in graph[curr]: #그래프 값으로 탐색
        if is_ward[next] == state: #next의 isward 값이 state와 같다면
            cnt += dfs(next, state) #cnt에 dfs결과 더해줌
    
    return cnt #cnt 리턴

def backtracking(cnt, true_area): #백트래킹 진행하는 함수
    global visited, ans #전역변수 선언
    # (기저조건) 모든 구역 탐색
    if cnt == n+1: #모든 구역 탐색했을 시
        if true_area == n: #True로 표시된 구역이 n개
            return
            
        false_node = is_ward.index(False) #값이 False인 것의 인덱스를 저장

        visited = [False] * (n+1) #방문했는지 검사하기 위한 리스트
        if true_area == dfs(1, True) and n - true_area == dfs(false_node, False): #true로 표시된 구역이 dfs(1,true)탐색결과와 같고 n에서 true area를 뺀 값이 dfs(false_node, False))와 같다면 
            ans = min(ans, calc_diff()) # 정답은 ans와 현재 인구수차이 중 작은 값
        return

    is_ward[cnt] = False #백트래킹 하기 전 false
    backtracking(cnt + 1, true_area) #다음cnt 재귀호출
    is_ward[cnt] = True #탐색 후 true로 갱신
    backtracking(cnt + 1, true_area + 1) #true+1해서 재귀호출
    return


# 입력

n = int(input()) #구역의 개수
people = list(map(int, ("0 " + input()).split())) #인구수  입력받아서 리스트로 저장
graph = [list() for _ in range(n+1)]    # 인접리스트
is_ward = [False] * (n+1) #False로 리스트 초기화해서 선언

for i in range(1, n+1): #1에서 n까지 반복
    graph[i] = list(map(int, input().split()[1:])) #입력값을 그래프에 리스트로 저장

# 연산
is_ward[0] = is_ward[1] = True    # 1번 구역 고정
backtracking(2, 1) #2,1로 백트래킹 시작

# 출력
if ans == INF:
    print(-1)
else:
    print(ans)