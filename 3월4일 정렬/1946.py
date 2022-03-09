case = int(input())

def decide(grade, n):
    count = n #지원자 수
    lose = set() #탈락하는 지원자
    
    for z in range(n):
        temp_grade = grade.copy() 
        del temp_grade[z] #1명의 지원자와 이 지원자와 비교할 남은 지원자들의 명단 
        
        for a in temp_grade.keys():
            if grade[z][0] > temp_grade[a][0] and grade[z][1] > temp_grade[a][1] : #이 지원자의 순위가 둘다 낮으면 탈락하는 지원자가 됨
                lose.add(z)
                
    count -= len(lose) #탈락자 수를 뺌
    print(count)

for i in range(case):
    
    n = int(input())
    grade = {} 
    
    for j in range(n):
        a, b = map(int, input().split()) #입력받은 점수를 딕셔너리로 저장
        grade[j] = [a,b]
        
    decide(grade, n)