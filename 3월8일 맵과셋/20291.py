n = int(input())

files = {} 

for i in range(n):
    name, ext = input().split('.')
#.으로 나눈 뒷부분(확장자)이 key이고 value는 등장한 횟수
    if ext in files :
        files[ext] += 1
    else :
        files[ext] = 1
    
files = sorted(files.items()) #확장자로 정렬

for i in files :
    print('{} {}'.format(i[0], i[1]))