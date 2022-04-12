n, k = map(int, input().split())
num = list(map(int,list(input())))

result = []

check = k #마지막 출력 시 k 쓰기 때문에 다른 변수 선언해서 사용
for i in range(n):
    while check > 0 and result: #처음실행시 result가 비어있으므로
        if result[-1] < num[i]: #result의 끝 수가 현재 비교하는 num의 값보다 작으면 pop
            result.pop()
            check -= 1
        else:
            break


    result.append(num[i]) 

for i in result[:n-k]: #앞에서부터 n-k자릿수까지 출력한다
    print(i,end='')