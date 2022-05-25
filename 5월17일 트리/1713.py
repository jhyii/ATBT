import sys
input = sys.stdin.readline #입력속도 위함

SIZE = 100 #학생최대번호

"""
 [후보 추천하기]

 1. 비어있는 사진틀이 없는 경우, 가장 추천수가 작은 학생 중 게시 시간이 오래된 학생을 삭제
 2. 후보 학생을 바로 찾기 위해 본 풀이는 딕셔너리 컨테이너를 사용해 구현

 !주의! 게시 시간 정보 저장 시, 후보로 올라간 가장 첫 시간을 저장. 이미 후보에 있는데 게시 시간이 갱신되지 않도록 주의.
"""

n = int(input()) #사진틀의 개수
k = int(input()) #전체 학생의 총 추천횟수
arr = list(map(int, input().split())) #추천학생번호 입력받아서 리스트에 저장

number = [0]*(SIZE + 1) #0리스트 선언
candidate = dict() #후보 딕셔너리

for idx, student in enumerate(arr):  #enumerate함수로 인덱스와 원소로 된 튜플 반복
    # 이미 사진이 올라와 있는 경우
    if student in candidate: #학생번호가 후보에 있다면
        candidate[student][0] += 1 #그 학생의 추천횟수 +1
    else: #새로운 후보라면
        if len(candidate) == n: #꽉 차있다면
            # 추천 횟수가 가장 적은 학생 찾기
            students = sorted(candidate.keys(), key=lambda x:candidate[x]) #key값으로 sort
            candidate.pop(students[0]) #가장 적은 학생 지우기
        candidate[student] = [1, idx] #새로운 후보 입력

print(*sorted(candidate.keys())) #추천수 증가하는 순서로 print