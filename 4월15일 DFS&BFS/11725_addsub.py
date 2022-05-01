import sys
sys.setrecursionlimit(10**8) #재귀 최대깊이 설정
input = sys.stdin.readline#input대체

"""
[트리의 부모 찾기]

- 1번 노드에서 출발해서 탐색
- 루트 노드에서 출발 했기 때문에, 현재 노드의 부모는 이전 노드가 된다.
- (주의) 트리 노드의 최대 수가 100,000이므로, 가능한 트리의 최대 깊이는 100,000번이 된다. 즉, 재귀 깊이 또한 100,000번이 되므로 재귀 깊이 제한을 재설정 해야한다.
"""

def dfs_recursion(prev, curr): #깊이우선탐색
    if parent[curr]: #부모노드가 0이 아니면, 즉 이미 구해졌으면
        return #함수 리턴
    
    parent[curr] = prev #현재꺼의 부모노드는 prev

    for next in adj_list[curr]: #curr번 노드 배열의 요소 꺼냄
        dfs_recursion(curr, next) #재귀 호출
    return #함수 리턴

n = int(input()) #노드의 개수 입력받음
adj_list = [list() for _ in range(n+1)] #노드의 개수 +1만큼 배열 생성해서 배열에 저장
parent = [0] * (n + 1) #부모노드 저장할 배열 초기화

for _ in range(n-1): #둘째줄부터 입력받음
    a, b = map(int, input().split()) #이 줄에서 연결된 두 정점 저장
    adj_list[a].append(b) #a번 노드의 배열에 b 추가, 연결되어있어서
    adj_list[b].append(a) #b번 노드 배열에 a 추가

dfs_recursion(1, 1)   # 1번 노드는 루트노드이므로, 부모를 자기 자신으로 설정
print(*parent[2:], sep='\n') #2번 노드부터 부모 출력