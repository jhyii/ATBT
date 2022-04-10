n, k = map(int, input().split())
num = list(map(int,list(input())))

max_index = num.index(max(num[:-(n-k-1)])) #가장 앞자리가 될 수의 인덱스
if max_index <= k:
    k -= max_index
    num = num[max_index:] #첫번째자리 앞의 수들을 다 지웁니다

while(k>0): #더 지울 수가 남아있을 때만 실행
    for j in range(len(num)-1):
        if num[j] < num[j+1]: #자릿수가 큰 쪽부터 비교해서 앞자리 수가 뒷자리 수보다 작을 때 지웁니다
            del num[j]
            k -= 1
            break
          
for i in num:
    print(i,end='')