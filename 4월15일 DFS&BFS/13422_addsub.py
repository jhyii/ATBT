import sys
input = sys.stdin.readline #input 대체

"""
 [도둑]
 1. 연속해서 훔쳐야 할 집이 m으로 고정됐기 때문에 슬라이딩 윈도우
 2. 직선이 아니라 원 형태의 배열! 모듈러 연산을 통해 윈도우의 양 끝 위치 조절하기
 !주의! 마을에 있는 집의 개수와 도둑이 훔칠 집의 개수가 같을 때(n==m) 도둑이 훔칠 수 있는 경우의 수 1개!
    => 예를 들어, n = m = 3, k = 4, house = [1, 1, 1] 일 때, 실제 방법의 수는 1번, 2번, 3번 집을 택하는 경우밖에 없지만
       예외 처리를 안해줄 경우, 원형으로 돌며 3을 출력하게 됨!
"""

def steal(n, m, k, house): #도둑이 훔칠 집 고르는 함수
    # 윈도우 초기화
    money = sum(house[:m]) #m-1집까지 가지고 있는 돈 액수 합
    count = 0 #카운트 0으로 초기화

    if money < k: #돈 액수 합이 k보다 작다면
        count += 1 #안 잡힐 수 있는 후보 +1

    if n == m: #만약 전체 집 수와 m이 같다면
        return count #count리턴

    for i in range(m, n + m -1): #m부터 n+m-1까지 전체 집 탐색
        money -= house[i - m] #액수 합에서 i-m 즉 제일 왼쪽 집의 액수 빼기
        money += house[i % n] #액수 합에 i%n번째 집이 가진 액수 더함 원형이니까

        if money < k: #더한 액수 합이 k보다 작다면
            count += 1 #카운트에 1을 더해줌
        
    
    return count #카운트 출력

# 입력
t = int(input()) #반복횟수 입력받음

for _ in range(t): #입력받은 수만큼 반복
    # 입력
    n, m, k = map(int, input().split()) #순서대로 집의 개수, 연속된 집의 개수, 최대 액수 입력받음
    house = list(map(int, input().split())) #각 집의 돈의 양 입력받음
    # 연산 + 출력
    print(steal(n, m, k, house)) #결과출력