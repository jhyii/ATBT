#import sys
#input = sys.stdin.readline


sieve = [True for i in range(1000001)]

for i in range(2, 1001): #100001**(1/2)로 하니까 런타임에러가 나서 그냥 값 넣음
    if sieve[i]:
        for j in range(2* 1000001, i):
            sieve[j] = False
   
while True:
    n = int(input())
    if n ==0: break
    success = 0
    
    for i in range(3, len(sieve)): #1,2도 True라서 3부터
        if sieve[i] and sieve[n-i]:
            print("{} = {} + {}".format(n,i,n-i))
            success = 1
            break
     
    if success == 0:
        print("Goldbach's conjecture is wrong.")
        break