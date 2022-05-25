import sys
input = sys.stdin.readline

n, m = map(int, input().split())

names = []
degrees = []
for i in range(n):
    name, degree = input().split()
    if degrees and degree == degrees[-1] : #점수가 같으면 저장 안함
        continue
    else:
        names.append(name)
        degrees.append(int(degree))
        
    

for i in range(m):
    left = 0
    right = len(degrees)-1
    
    num = int(input())
    while left<=right: #이분탐색
        mid = (left+right)//2
        
        if degrees[mid] >= num:
            right = mid-1
        else:
            left = mid+1
            
    
    print(names[right+1]) #출력값이 상한과 같아서