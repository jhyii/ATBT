from collections import deque
N, d, k, c = map(int,(input().split()))

arr = []

for i in range(N):
    arr.append(int(input()))

arr = arr+ arr[:k-1]

window = deque()
MAX = 1
    
for i in range(k):
    window.append(arr[i])

set_window = set(window)
set_window.add(c)
MAX = max(MAX, len(set_window))
    
for i in range(k,N+k-1):
    window.popleft() #이번 윈도우에서 제외되는 값
    window.append(arr[i]) #이번 윈도우에서 추가되는 값
        
    set_window = set(window)
    set_window.add(c)
    MAX = max(MAX, len(set_window))

print(MAX)