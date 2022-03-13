import sys
import re

input = sys.stdin.readline

# 각 시간을 정수형태로 저장
s, e, q = input().split()
s = int(re.sub(":","",s))
e = int(re.sub(":","",e))
q = int(re.sub(":","",q))

in_streaming = set() # 스트리밍에 들어온 닉네임 중복없이 저장할 셋
count = 0

while True:
    time, name = input().split()
    time = int(re.sub(":","",time))
# 조건에 맞게 카운트
    if time <= s :
        in_streaming.add(name)
    elif e <= time <= q and name in in_streaming:
        count += 1
        
print(count)