case = int(input())

dot = []

for i in range(case):
    a, b = map(int, input().split()) #입력받은 점을 리스트로 저장
    dot.append((a,b))
    
dot.sort(key=lambda x:(x[1],x[0])) #y같을 때 x오름차순

for d in dot:
    print(d[0], d[1])
