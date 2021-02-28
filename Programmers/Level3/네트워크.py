"""
참고 자료
https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-DFS-BFS-Python 
"""
# bfs로 구현

def bfs(n, computer, com, visit):
    visit[com] = True
    queue = []
    queue.append(com)

    while queue:
        com = queue.pop(0)
        visit[com] = True
        for con in range(n):
            if con != com and computer[com][con] == 1:
                if visit[con] == False:
                    queue.append(con)

def solution(n, computers):
    cnt = 0
    visit = [0 for _ in range(n)]

    for com in range(n):
        if visit[com] == 0:
            bfs(n, computers, com, visit)
            cnt += 1
    return cnt
