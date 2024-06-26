from collections import deque

n, m = map(int, input().split()) #세로, 가로
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4): #현재 위치에서 네 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: #공간 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: #해당 노드 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1] # 가장 오른쪽 아래까지의 최단 거리 반환
print(bfs(0, 0))
