n = int(input())
dist = list(map(int,input().split())) #주유소 사이 거리
stat = list(map(int,input().split())) #주유소의 리터당 가격

price = stat[0]*dist[0] #처음엔 무조건 처음 가야하는 거리만큼 첫 주유소에서 산다
my_gas = dist[0] #내가 보유하고있는 가스

min_stat = [0]*len(stat) #현재까지 주유소 가격 중 가장 싼 가격을 저장하는 배열
min_stat[0] = stat[0]
for i in range(1,len(stat)):
    if stat[i] < min_stat[i-1]:
        min_stat[i] = stat[i]
    else:
        min_stat[i] = min_stat[i-1]


for i in range(1, n-1):
    my_gas -= dist[i-1] #한칸 전진하면서 지나온 만큼 가스를 사용한다
    if my_gas < dist[i]: #보유하고 있는 가스가 가야하는 거리보다 적어 사야하는 경우
        necess = dist[i] - my_gas #필요한 가스 양
        price += min_stat[i]*necess #필요한 가스 양만큼 앞의 주유소 중 가장 싼 곳에서 산 걸로 친다
        my_gas += necess #보유하는 가스 양이 산만큼 많아진다
    
print(price)