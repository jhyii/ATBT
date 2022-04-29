numbers = list(input()) #리스트로 변환

if '0' not in numbers: #10의 배수라면 0이 있어야 함
    print(-1)

else: 
    sum = 0
    for i in numbers:
        sum += int(i)

    if sum%3 != 0: #3의 배수 확인
        print(-1)
    else:
        sorted_num = sorted(numbers, reverse=True) #가장 큰 수 출력하기 위해
        answer = "".join(sorted_num)
        print(answer)