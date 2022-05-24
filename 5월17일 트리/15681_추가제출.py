import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

"""
 PPT 트리의 정점의 수 구하기 응용

 [트리와 쿼리]

 1. 루트에서부터 dfs 탐색
 2. 각 노드를 루트로 하는 서브트리의 정점 수를 재귀적으로 계산
    - 서브트리에 속한 정점의 개수를 저장하는 dp 배열의 초기화를 -1로 해주고, dfs 탐색 시 현재 정점의 dp 값을 0으로 설정함으로써 자식 노드만 탐색할 수 있도록 함 (부모 노드에 0이 저장되어 있으므로 바로 리턴)
"""

def tree_dp(curr, graph): #서브트리의 정점 수 계산하는 함수
    if subtree_cnt[curr] != -1: #탐색한 점이라면
        return subtree_cnt[curr] #탐색했던 값 출력

    # 서브트리에 속한 정점의 수를 세고, 저장
    subtree_cnt[curr] = 0   # 현재 노드를 0으로 표기하여 부모 자식간 계속 호출되지 않도록
    cnt = 1 #cnt 1로 초기화
    for next in graph[curr]: #현재 그래프의 리스트로 반복
        cnt += tree_dp(next, graph) #재귀호출하며 더해줌

    subtree_cnt[curr] = cnt #호출이 끝나면 서브트리정점수 저장
    return cnt #cnt 출력


# 입력
n, r, q = map(int, input().split()) #트리의 정점의 수, 루트의 번호, 쿼리의 수 입력받음
graph = [list() for _ in range(n+1)] #리스트의 리스트로 그래프 선언 
subtree_cnt = [-1]*(n+1) #-1로 된 subtree표시할 리스트 선언

for _ in range(n-1): #n-1번 반복
    u, v = map(int, input().split()) #트리에 속한 간선의 정보
    graph[u].append(v) #그래프의 u 인덱스에 v append
    graph[v].append(u) #그래프의 v 인덱스에 u append

# 연산
tree_dp(r, graph) #함수 호출


# 출력
for _ in range(q):
    print(subtree_cnt[int(input())]) #정답 출력