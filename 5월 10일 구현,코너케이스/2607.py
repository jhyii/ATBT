import sys
from collections import Counter #개수 세는 도구
input = sys.stdin.readline #인풋속도 줄임

SIZE = 26 #알파벳 개수

"""
 [비슷한 단어]

 단어가 같은 구성일 조건
 1. 두 개의 단어가 같은 종류의 문자로 이루어짐
 2. 같은 문자는 같은 개수만큼 있음

 비슷한 단어의 조건
 1. 한 단어에서 한 문자를 더하거나, 빼면 같은 구성이 됨
    -> 두 단어에서 다른 문자의 개수가 총 1개
 2. 한 단어에서 한 문자를 바꾸면 같은 구성이 됨
    -> 두 단어에서 다른 문자의 개수가 총 2개
    -> !주의! 이때, 두 단어의 길이가 같아야 함 cf) doll | do

 <Counter>
 - iterable한 객체를 받아서 횟수를 기록하여 Counter 객체로 반환.
 - 이때 Counter 객체는 유사 dictionary라고 생각할 수 있다.
 - 주의할 점은, 일반 dictionary와는 다르게 default 값이 0으로 설정되어 있어, 삽입하지 않은 키 값에 대한 조회가 가능하다.
"""

# 입력
n = int(input()) #단어개수 입력받음

source = input().rstrip() #기준이 되는 첫 번째 단어 입력
source_cnt = Counter(source) #첫 번째 단어의 알파벳개수 저장
ans = 0 #정답 초기화

alphabets = [chr(i + ord('A')) for i in range(SIZE)]    # 알파벳 리스트

for _ in range(n-1): #n-1번동안 단어 입력받음
    target = input().rstrip() #비교할 단어
    diff = 0 #다른 알파벳 카운트할 변수
    target_cnt = Counter(target) #비교할 단어 알파벳 개수 저장

    for key in alphabets: #알파벳 하나씩 반복
        diff += abs(target_cnt[key] - source_cnt[key])  # Counter 객체이므로 키가 존재하는지 확인 불필요
    
    if diff <= 1 or (diff == 2 and len(target) == len(source)): #차이가 1보다 작거나 같거나, 차이가 두 개인데 두 단어의 길이가 같을 때
        ans += 1 #이 단어는 비슷한 단어임
    
print(ans) #정답 출력