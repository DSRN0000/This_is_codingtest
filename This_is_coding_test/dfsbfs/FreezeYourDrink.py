n, m = map(int, input().split()) #세로,가로
graph = list(list(map(int, input())) for _ in range(n))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 #노드 방문하지 않았다면 방문처리
        #상하좌우 위치도 재귀적으로 호출
        dfs(x - 1, y) #상
        dfs(x + 1, y) #하
        dfs(x, y - 1) #좌
        dfs(x, y + 1) #우
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)