def dfs(graph, v, visited): #dfs 메서드 정의
    visited[v] = True #현재 노드 방문처리
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]] #각 노드가 연결된 정보를 리스트 자료형으로 표현
visited = [False] * 9 #방문 정보

dfs(graph, 1, visited)