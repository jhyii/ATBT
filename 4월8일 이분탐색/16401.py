import sys
input = sys.stdin.readline

m, n = map(int,input().split())
candy = list(map(int,input().split()))

left = 0
right = max(candy)

while left<=right:
    mid = (left+right)//2
    count = 0
    
    if mid==0: #나눠줄 수 없는 경우
        left = 1 #출력값이 left-1이라서
        break
        
    for i in candy:
        if i>=mid:
            count += i//mid #자를 수 있으니까
    
    if count >= m:
        left = mid+1
    else:
        right = mid-1
        
print(left-1)