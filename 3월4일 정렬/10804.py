list = [i for i in range(1, 21)]

def sort_list(start, end, list):
    temp_list = list.copy()
    for i in range(start,end+1):
        list[i-1] = temp_list[start+end-i-1]

for j in range(10):
    start, end = map(int, input().split())
    sort_list(start, end, list)
    
for i in list:
    print(i, end=' ')