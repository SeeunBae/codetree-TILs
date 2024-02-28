import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[0]*(n+1)
sum=0

def dfs(a):
    global sum
    visited[a] = 1
    for i in graph[a]:
        if visited[i]==0:
            sum+=1
            dfs(i)

dfs(1)
print(sum)