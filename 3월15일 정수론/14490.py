n, m = map(int,input().split(':'))

def gcd(n,m): #유클리드호제법
    while(m):
        n %= m
        n, m = m, n
        
    return n

print("{}:{}".format(n//gcd(n,m), m//gcd(n,m)))