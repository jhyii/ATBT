SIZE = 10 #과녁개수

"""
 [양궁대회]
 
 1. 가능한 모든 경우를 백트래킹 탐색을 통해 검사
 -> 라이언이 점수를 얻어가려면 어피치보다 1개 더 쏘는 경우가 최적. 어피치보다 적게 화살 쏘는 건 점수 못 얻어가므로 어차피 의미가 없음.
 -> 따라서 라이언이 각 점수에 화살을 아래와 같이 쏘는 2가지 경우만 고려해서 만들어지는 모든 경우를 백트래킹으로 탐색
    - 어피치가 점수 획득을 하는 경우: 해당 점수에는 화살을 한 발도 쏘지 않는 것이 이득
    - 라이언이 점수 획득을 하는 경우: 필요한 최소 화살을 사용하는 것이 이득이므로 어피치보다 정확히 한 발 더 쏨

 !주의! 0번 인덱스가 10점 과녁임을 주의
"""

max_diff = 1 #최대diff
answer = [-1] #정답 배열 선언


def backtracking(idx, left, diff, ryan, appeach): #백트래킹 진행하는 함수
    global max_diff, answer #전역변수 선언
    # 기저조건 - 0점 과녁까지 모두 탐색한 경우
    if idx == SIZE: #idx가 10일 경우
        ryan[idx] = left #라이언 과녁 left로 옮기기
        
        if diff > max_diff: #최대깊이보다 크다면
            max_diff = diff #최대를 갱신
            answer = ryan[:] #정답에 라이언과녁 넣기
        elif diff == max_diff: #최대랑 같다면
            if ryan[::-1] > answer[::-1]: #라이언 과녁이 정답보다 크다면
                answer = ryan[:] #갱신해줌
        return
    
    # 남은 화살로 라이언이 점수를 얻을 수 있는 경우
    if left > appeach[idx]: #만약 어피치의 점수가 left보다 작다면
        ryan[idx] = appeach[idx] + 1 #라이언은 한개 더 쏨
        backtracking(idx+1, left - ryan[idx], diff + SIZE - idx, ryan, appeach) #재귀호출
        ryan[idx] = 0 #0으로 갱신

    # 어피치가 점수를 얻을 수 있는 경우 점수 계산
    if appeach[idx]: #어피치 점수가 존재할 때
        diff -= SIZE - idx #diff값에서 전체 길이에서 현재 idx 뺀 값을 뺀다
    backtracking(idx+1, left, diff, ryan, appeach) #다음 idx 재귀호출
    return

def solution(n, info):
    ryan = [0]*11   # 라이언 과녁 정보
    backtracking(0, n, 0, ryan, info) #백트래킹으로 라이언이 쏴야하는 과녁 검사
    
    return answer #라이언의 과녁 리턴


# 디버깅 위한 메인 코드 - 프로그래머스에는 제출 X
if __name__ == "__main__":
    n = 5 #어피치가 지금까지 쏜 화살
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0] #어피치 과녁 정보

    print(*solution(n, info)) #solution함수 결과 리턴