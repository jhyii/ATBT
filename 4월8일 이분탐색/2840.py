n, k = map(int,input().split())
input_arr = []

for i in range(k):
    s, alph = input().split()
    input_arr.append([s, alph])
    
result = ['?' for i in range(n)]
index = 0
result_bool = True

for i in input_arr:
    if int(i[0]) > n-index-1: #한 바퀴 넘어가는 경우
        index = (index + int(i[0]))%n
        if result[index] != '?' and result[index] != i[1]: #들어있는 값이 ?가 아닌데 같은 값이 아닌 경우
            result_bool = False
        else:
            result[index] = i[1]
    else:
        index += int(i[0])
        if result[index] != '?' and result[index] != i[1]:
            result_bool = False
        else:
            result[index] = i[1]

#중복검사
test_arr = result.copy()
remove_set = {'?'}
test_arr = [i for i in test_arr if i not in remove_set]

test_set = set(test_arr)
if len(test_arr) != len(test_set):
    result_bool = False

if result_bool == False:
    print('!')
else:
    for i in range(n): #화살표 돌아가는 방향과 반대로 읽으므로 반대로 프린트
        if index < 0:
            index += n
            
        print(result[index], end='')
        index -= 1