import sys
input = sys.stdin.readline
n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]

def total(row_s, col_s, row_e, col_e):
    sum=0
    for i in range(row_s, row_e+1):
        for j in range(col_s, col_e+1):
            sum+=graph[i][j]
    return sum

result=0
for i in range(n):
    for j in range(n):
        if i+2>=n or j+2>=n:
            continue
        num=total(i, j, i+2, j+2)
        result=max(result, num)

print(result)