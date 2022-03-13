case = int(input())

numbers = []

for i in range(case):
    num = input()
    numbers.append(num)
    
def sum(number): #두 번째 조건 충족을 위한 함수
    result = 0
    for i in number:
        if i.isdigit():
            result += int(i)
    return result

numbers.sort(key = lambda x:(len(x), sum(x), x))

for i in numbers:
    print(i)