import sys
input = sys.stdin.readline

n, length = map(int,input().split())

wordlist = {}
for i in range(n):
    word = input()
    if len(word) >= length:
        if word in wordlist:
            wordlist[word] += 1
        else :
            wordlist[word] = 0
            
sorted_wordlist = sorted(wordlist.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
#value값인 빈도가 첫번째, 단어길이가 두번째, 단어알파벳순서가 세번째 우선순위로 정렬

for i in sorted_wordlist:
    print(i[0])