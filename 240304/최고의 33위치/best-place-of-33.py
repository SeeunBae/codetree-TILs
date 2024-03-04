import sys
input = sys.stdin.readline
n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]

def total(x, y):
    sum=0
    if x+2>=n or y+2>=n:
        return 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if graph[i][j] == 1:
                sum+=1
    return sum

result=0
for i in range(n):
    for j in range(n):
        result = max(result, total(i, j))
    
print(result)