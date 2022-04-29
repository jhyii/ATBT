import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arr.sort()

def sum_liquid(N, arr):
    
    MIN = float("inf")
    answer = []

    for i in range(N):
        temp_arr = arr.copy()
        temp_arr.pop(i)
    
        left = 0
        right = N-2
    
        while left < right:
            result = temp_arr[left] + temp_arr[right] + arr[i]
            if result == 0: # 값이 0이라면 이보다 더 0에 가까워질 수는 없기 때문에 바로 리턴
                sort_answer = [temp_arr[left], temp_arr[right], arr[i]]
                sort_answer.sort()
                return sort_answer
                break
        
            if (abs(result) < MIN):#0에 가까운 값을 갱신할 수 있는지 확인
                MIN = abs(result)
                answer = [temp_arr[left], temp_arr[right], arr[i]]
            if result > 0: #0보다 크다면 더 작은 값을 만들어야 함 -> right 이동
                right -= 1
            else: #0보다 작다면 더 큰 값을 만들어야 함 -> left 이동
                left += 1
    
    answer.sort()
    return answer

for i in sum_liquid(N, arr):
    print(i, end=' ')