import sys


def DFS(root):
    print(root, end=' ')
    visit[root] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and graph[root][i] == 1:
            DFS(i)


def BFS(root):
    queue = [root]
    visit[root] = 0

    while queue:
        root = queue[0]
        print(root, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and graph[root][i] == 1:
                queue.append(i)
                visit[i] = 0


# 정점의 갯수 N, 간선의 갯수 M, root V
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

# 연결 된 node 값을 1로 변경
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

DFS(v)
print()
BFS(v)
