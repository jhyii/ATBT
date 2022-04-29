n = int(input())
arr = list(map(int,input().split()))
arr.sort()

count = 0
for i in range(n):
    temp = arr.copy()
    temp.pop(i) #자기자신 제거
    left, right = 0, len(temp)-1
    
    while left<right:
        result = temp[left]+temp[right]
        if result == arr[i]:
            count += 1
            break   
        elif result > arr[i]:
            right -= 1
        else:
            left += 1
            
print(count)