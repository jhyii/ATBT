from itertools import permutations

n = int(input())

innings = []
for i in range(n):
    innings.append(list(map(int,input().split())))
    
def progress(sign): #아웃~홈런 진행하는 함수
    global score, out, base_1, base_2, base_3 #전역변수 사용
    if sign == 0: #아웃
        out += 1
    elif sign == 1: #1루타
        score += base_3
        base_3 = base_2
        base_2 = base_1
        base_1 = 1
    elif sign == 2: #2루타
        score += (base_3 + base_2)
        base_3 = base_1
        base_2 = 1
        base_1 = 0
    elif sign == 3: #3루타
        score += (base_3 + base_2 + base_1)
        base_3 = 1
        base_2 = 0
        base_1 = 0
    elif sign == 4: #홈런
        score += (base_3 + base_2 + base_1 + 1)
        base_3 = 0
        base_2 = 0
        base_1 = 0
    
    
def game(players): #이닝 반복하며 게임점수 리턴하는 함수
    global score #전역변수
    hitter = 0
    score = 0
    
    for inning in innings:
        global out, base_1, base_2, base_3 #전역변수
        out = 0
        base_1, base_2, base_3 = 0, 0, 0
        
        while out<3 :
            progress(inning[players[hitter]]) #함수호출
            hitter = (hitter+1)%9 #다음 선수로 넘어감
                
    return score    
   
max_score = 0 
    
p_list = list(permutations(range(1,9), 8)) #브루트포스,, 모든 조합 다 해보기
for p in p_list:
    players = list(p[:3]) + [0] + list(p[3:]) #1번(인덱스0)선수는 4번타자 고정
    max_score = max(max_score, game(players)) #지금까지 max와 비교

print(max_score)