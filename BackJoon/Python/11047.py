import sys

n, k = map(int, sys.stdin.readline().split())
money = []
cnt = 0

for _ in range(n):
    money.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):
    cnt += k//money[i]
    k %= money[i]
print(cnt)
