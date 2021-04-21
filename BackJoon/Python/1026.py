import sys

s = 0
idx = 0

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort()


for i in a:
    s += i * b[idx]
    idx += 1
    
print(s)