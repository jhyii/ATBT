import sys
input = sys.stdin.readline #입력속도 위함
sys.setrecursionlimit(10**8) #최대 재귀호출 횟수

"""
 [트리의 지름]

 1. 지름을 이루는 두 점은 모두 리프 노드
 2. 임의의 한 노드에서 가장 멀리 있는 노드(리프 노드)는 지름을 이루는 노드 중 하나
 3. 지름을 이루는 노드에서 가장 멀리 있는 노드는 지름을 이루는 다른 노드

 부모->자식의 방향만 저장하면 리프 노드에서 다른 리프 노드로 탐색할 수 없으므로 무방향 그래프로 저장
"""

def dfs(node, parent, graph): #노드, 부모노드, 자식노드 입력받아서 dfs탐색
    pos = node #현재 노드
    dist = 0 #거리 초기화
    for next, weight in graph[node]: #현재 노드와 연결되어있는 노드들
        if next == parent: #부모노드라면
            continue #넘어감
        
        child_node, child_dist = dfs(next, node, graph) #현재노드를 부모로하는 다음노드에서 재귀호출

        if weight + child_dist > dist: #현재 가중치를 더했을 때 거리보다 크다면
            dist = weight + child_dist #거리 갱신
            pos = child_node #노드 옮김

    return pos, dist #다음노드와 거리 출력

# 입력
n = int(input()) #노드의 개수

graph = [list() for _ in range(n+1)] #길이가 n인 리스트의 리스트 선언

for _ in range(n-1): #반복
    p, c, w = map(int, input().split()) #부모노드, 자식노드, 가중치
    # 무방향 그래프로 만들기
    graph[p].append((c, w)) #부모노드 인덱스에 자식노드와 가중치를 튜플로 저장
    graph[c].append((p, w)) #자식노드 인덱스에 부모노드와 가중치를 튜플로 저장

# 연산
first_node, _ = dfs(1, -1, graph) #dfs로 탐색 후 정답의 첫번째 노드가 될 노드 저장
_, radius = dfs(first_node, -1, graph) #위에서 찾은 노드부터의 지름 저장

print(radius) #정답 프린트