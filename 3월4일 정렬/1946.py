case = int(input())

for i in range(case):

    n = int(input())
    grade = []

    for j in range(n):
        a, b = map(int, input().split()) #입력받은 점수를 이중리스트로 저장
        grade.append([a,b])

    grade.sort() #첫번째등수로 정렬
    max = grade[0][1] #첫번째등수 1등인 사람의 두번째등수 기준
    count = 1 #1등은 무조건 합격이라 카운트

    for i in range(1,len(grade)):
        if grade[i][1] < max : #두번째등수가 max보다 작으면 합격
            count += 1
            max = grade[i][1] #다음 사람은 첫번째 등수 바로 앞의 사람과 두번째등수를 비교해야함

    print(count)
