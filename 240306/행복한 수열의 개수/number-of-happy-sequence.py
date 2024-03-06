import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]


def col():
    c_sum=0
    for i in range(n):
        num=0
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                num+=1
        if num>=m-1:
            c_sum+=1
    return c_sum


def row():
    r_sum=0
    for i in range(n):
        num=0
        for j in range(n-1):
            if graph[j][i] == graph[j+1][i]:
                num+=1
        if num>=m-1:
            r_sum+=1
    return r_sum

print(col()+row())