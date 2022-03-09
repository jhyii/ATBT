h, m, s = map(int, input().split()) #현재시간 입력받음
n = int(input())

TOTAL_SEC = h*3600 + m*60 + s #현재시간을 초로 계산해놓기
UPPER_SEC = 24*3600 

def time_cul(): #전체 초로 시간,분,초를 계산하는 함수
    global TOTAL_SEC, UPPER_SEC
    while TOTAL_SEC < 0 or TOTAL_SEC > UPPER_SEC : #전체 초가 마이너스이거나 24시간을 넘는 경우
        if TOTAL_SEC < 0 : #전체 초가 마이너스인 경우 24시간에 해당하는 초를 더해준다
            TOTAL_SEC += UPPER_SEC
        elif TOTAL_SEC > UPPER_SEC : #전체 초가 24시간보다 넘는 경우 24시간에 해당하는 라운드만큼 초를 없애준다
            TOTAL_SEC %= UPPER_SEC
        
    hour = int(TOTAL_SEC/3600) #전체 초를 3600초로 나눈 몫
    minute = int((TOTAL_SEC%3600)/60) #전체 초를 3600초로 나눈 나머지를 다시 60초로 나눈 몫
    second = int(TOTAL_SEC%60) #전체 초를 60초로 나눈 나머지
    
    print(hour, minute, second)
    
for i in range(n):
    query = input()
    
    if query[0] == '1':
        TOTAL_SEC += int(query[2:]) #전체 초에 더해준다
    elif query[0] == '2':
        TOTAL_SEC -= int(query[2:]) #전체 초에서 빼준다
    elif query[0] == '3':
        time_cul()