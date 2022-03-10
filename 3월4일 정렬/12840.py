import datetime

h, m, s = map(int, input().split()) #현재시간 입력받음
n = int(input())

TOTAL_SEC = h*3600 + m*60 + s #현재시간을 초로 계산해놓기

def time_cul(): #전체 초로 시간,분,초를 계산하는 함수
    global TOTAL_SEC
    time_str = (lambda x : '0' + x if len(x) < 8 else x )(str(datetime.timedelta(seconds=TOTAL_SEC)))

    hour = int(time_str[:2])
    minute = int(time_str[3:5])
    second = int(time_str[6:8])

    print(hour, minute, second)

for i in range(n):
    query = input()

    if query[0] == '1':
        TOTAL_SEC += int(query[2:]) #전체 초에 더해준다
    elif query[0] == '2':
        TOTAL_SEC -= int(query[2:]) #전체 초에서 빼준다
    elif query[0] == '3':
        time_cul()
