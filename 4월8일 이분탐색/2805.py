import sys
input = sys.stdin.readline #안 하면 시간초과남

n, m = map(int,input().split())
trees = list(map(int,input().split()))

left = 1
right = max(trees)

while left<=right:
    mid = (left+right)//2
    
    cutted = 0
    for tree in trees: #반복을 통해 잘라가는 나무 길이 저장
        if tree > mid:
            cutted += (tree-mid)
    
    if cutted >= m: #이분탐색
        left = mid+1
    else:
        right = mid-1
        
print(right) #나무의 최대높이