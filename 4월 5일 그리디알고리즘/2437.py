n = int(input())
chu = list(map(int, input().split()))
chu.sort()

result = 0
for i in range(n):
    
    if (result+1) >= chu[i]: #result는 여태까지 추의 합
        result += chu[i] #추의 무게가 여태까지 추의 합+1보디 작거나 같다면 앞의 조합들로 구할 수 있음
    else:
        break

print( result +1 )