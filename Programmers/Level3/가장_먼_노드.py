# BFS로 풀이
from collections import deque

def bfs(v, visited, graph):
    count = 0
    queue = deque([[v, count]])
    while queue:
        value = queue.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for node in graph[v]:
                queue.append([node, count])

def solution(n, edge):
    answer = 0
    visited = [-1 for _ in range(n+1)]
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        graph[x].append(y)
        graph[y].append(x)
    bfs(1, visited, graph)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer
