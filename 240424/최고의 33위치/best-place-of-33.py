n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def num_of_gold(row_s, row_e, col_s, col_e):
    num_of_gold = 0
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            num_of_gold += graph[row][col]
    return num_of_gold


max_num = 0
for row in range(n):
    for col in range(n):
        if row+2>=n or col+2>=n:
            continue
        num = num_of_gold(row, row+2, col, col+2)
        max_num = max(max_num, num)

print(max_num)