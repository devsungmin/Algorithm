import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for i in range(n+1)]
p = [0 for _ in range(n+1)]  # 부모 정보 저장 리스트

for _ in range(n-1):
    left, right = list(map(int, sys.stdin.readline().split()))
    tree[left].append(right)
    tree[right].append(left)

queue = deque()
queue.append(1)

while queue:
    tmp = queue.popleft()

    for i in tree[tmp]:
        if p[tmp-1] != i:
            p[i-1] = tmp
            queue.append(i)

for i in range(1, n):
    print(p[i])
