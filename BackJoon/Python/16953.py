''' 풀이 참고
https://donghak-dev.tistory.com/90
'''
# bfs로 풀이
import sys
from collections import deque

def bfs(a):
    visited = []

    que = deque()
    que.append([0, a])
    visited.append(a)

    while que:
        cnt, num = que.popleft()

        if num == b:
            return cnt + 1
        for n in (num * 2, int(str(num) + '1')):
            if n <= b:
                if n not in visited:
                    que.append([cnt + 1, n])
                    visited.append(n)
    return -1

a, b = map(int, sys.stdin.readline().split())
print(bfs(a))
